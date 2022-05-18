#include <stdio.h>
int main()
{
#ifdef _WIN32
	printf("Windows OS\n");
#elif __APPLE__
	printf("Mac OS\n");
#elif __linux__
	printf("Linux OS\n");
#elif TARGET_OS_EMBEDDED
	printf("IOS embedded OS\n");
#elif TARGET_IPHONE_SIMULATOR
	printf("IOS simulator OS\n");
#elif TARGET_OS_IPHONE
	printf("iPhone OS\n");
#elif TARGET_OS_MAC
	printf("MAC OS\n");
#elif__ANDROID__
	printf("android OS.\n");
#elif __unix__
	printf("unix OS\n");
#elif _POSIX_VERSION
	printf("POSIX based OS\n");
#elif __sun
	printf("Solaris OS\n");
#elif __hpux
	printf("HP UX OS\n");
#elif BSD
	printf("Solaris OS\n");
#elif __DragonFly__
	printf("DragonFly BSD OS\n");
#elif __FreeBSD__
	printf("FreeBSD OS\n");
#elif __NetBSD__
	printf("Net BSD OS\n");
#elif __OpenBSD__
	printf("Open BSD OS\n");
#else
	printf("Sorry, the system are"
		"not listed above.\n");
#endif
	return 0;
}
