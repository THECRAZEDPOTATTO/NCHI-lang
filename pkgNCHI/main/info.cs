using System.Management;
using System;
using System.IO;
using System.Net.NetworkInformation;
ManagementObjectSearcher myVideoObject = new ManagementObjectSearcher("select * from Win32_VideoController");

foreach (ManagementObject obj in myVideoObject.Get())
{
    Console.WriteLine("Name  -  " + obj["Name"]);
    Console.WriteLine("Status  -  " + obj["Status"]);
    Console.WriteLine("Caption  -  " + obj["Caption"]);
    Console.WriteLine("DeviceID  -  " + obj["DeviceID"]);
    Console.WriteLine("AdapterRAM  -  " + obj["AdapterRAM"]);
    Console.WriteLine("AdapterDACType  -  " + obj["AdapterDACType"]);
    Console.WriteLine("Monochrome  -  " + obj["Monochrome"]);
    Console.WriteLine("InstalledDisplayDrivers  -  " + obj["InstalledDisplayDrivers"]);
    Console.WriteLine("DriverVersion  -  " + obj["DriverVersion"]);
    Console.WriteLine("VideoProcessor  -  " + obj["VideoProcessor"]);
    Console.WriteLine("VideoArchitecture  -  " + obj["VideoArchitecture"]);
    Console.WriteLine("VideoMemoryType  -  " + obj["VideoMemoryType"]);
}
Console.WriteLine("AdapterRAM  -  " + SizeSuffix((long)Convert.ToDouble(obj["AdapterRAM"])));
DriveInfo[] allDrives = DriveInfo.GetDrives();

foreach (DriveInfo d in allDrives)
{
    Console.WriteLine("Drive {0}", d.Name);
    Console.WriteLine("  Drive type: {0}", d.DriveType);
    if (d.IsReady == true)
    {
        Console.WriteLine("  Volume label: {0}", d.VolumeLabel);
        Console.WriteLine("  File system: {0}", d.DriveFormat);
        Console.WriteLine("  Available space to current user:{0, 15} bytes", d.AvailableFreeSpace);

        Console.WriteLine("  Total available space:          {0, 15} bytes", d.TotalFreeSpace);

        Console.WriteLine("  Total size of drive:            {0, 15} bytes ", d.TotalSize);
        Console.WriteLine("  Root directory:            {0, 12}", d.RootDirectory);
    }
}
static readonly string[] SizeSuffixes = { "bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB" };

static string SizeSuffix(Int64 value)
{
    if (value < 0) { return "-" + SizeSuffix(-value); }
    if (value == 0) { return "0.0 bytes"; }

    int mag = (int)Math.Log(value, 1024);
    decimal adjustedSize = (decimal)value / (1L << (mag * 10));

    return string.Format("{0:n1} {1}", adjustedSize, SizeSuffixes[mag]);
}
Console.WriteLine("  Available space to current user:{0, 15}", SizeSuffix(d.AvailableFreeSpace));
Console.WriteLine("  Total available space:          {0, 15}", SizeSuffix(d.TotalFreeSpace));
Console.WriteLine("  Total size of drive:            {0, 15} ", SizeSuffix(d.TotalSize));
ManagementObjectSearcher myProcessorObject = new ManagementObjectSearcher("select * from Win32_Processor");

foreach (ManagementObject obj in myProcessorObject.Get())
{
    Console.WriteLine("Name  -  " + obj["Name"]);
    Console.WriteLine("DeviceID  -  " + obj["DeviceID"]);
    Console.WriteLine("Manufacturer  -  " + obj["Manufacturer"]);
    Console.WriteLine("CurrentClockSpeed  -  " + obj["CurrentClockSpeed"]);
    Console.WriteLine("Caption  -  " + obj["Caption"]);
    Console.WriteLine("NumberOfCores  -  " + obj["NumberOfCores"]);
    Console.WriteLine("NumberOfEnabledCore  -  " + obj["NumberOfEnabledCore"]);
    Console.WriteLine("NumberOfLogicalProcessors  -  " + obj["NumberOfLogicalProcessors"]);
    Console.WriteLine("Architecture  -  " + obj["Architecture"]);
    Console.WriteLine("Family  -  " + obj["Family"]);
    Console.WriteLine("ProcessorType  -  " + obj["ProcessorType"]);
    Console.WriteLine("Characteristics  -  " + obj["Characteristics"]);
    Console.WriteLine("AddressWidth  -  " + obj["AddressWidth"]);
}
ManagementObjectSearcher myOperativeSystemObject = new ManagementObjectSearcher("select * from Win32_OperatingSystem");

foreach (ManagementObject obj in myOperativeSystemObject.Get())
{
    Console.WriteLine("Caption  -  " + obj["Caption"]);
    Console.WriteLine("WindowsDirectory  -  " + obj["WindowsDirectory"]);
    Console.WriteLine("ProductType  -  " + obj["ProductType"]);
    Console.WriteLine("SerialNumber  -  " + obj["SerialNumber"]);
    Console.WriteLine("SystemDirectory  -  " + obj["SystemDirectory"]);
    Console.WriteLine("CountryCode  -  " + obj["CountryCode"]);
    Console.WriteLine("CurrentTimeZone  -  " + obj["CurrentTimeZone"]);
    Console.WriteLine("EncryptionLevel  -  " + obj["EncryptionLevel"]);
    Console.WriteLine("OSType  -  " + obj["OSType"]);
    Console.WriteLine("Version  -  " + obj["Version"]);
}
NetworkInterface[] nics = NetworkInterface.GetAllNetworkInterfaces();

if (nics == null || nics.Length < 1)
{
    Console.WriteLine("  No network interfaces found.");
}else{
    foreach (NetworkInterface adapter in nics)
    {
        IPInterfaceProperties properties = adapter.GetIPProperties();
        Console.WriteLine();
        Console.WriteLine(adapter.Description);
        Console.WriteLine(String.Empty.PadLeft(adapter.Description.Length, '='));
        Console.WriteLine("  Interface type .......................... : {0}", adapter.NetworkInterfaceType);
        Console.WriteLine("  Physical Address ........................ : {0}", adapter.GetPhysicalAddress().ToString());
        Console.WriteLine("  Operational status ...................... : {0}", adapter.OperationalStatus);
    }
}
public static void ShowNetworkInterfaces()
{
    IPGlobalProperties computerProperties = IPGlobalProperties.GetIPGlobalProperties();
    NetworkInterface[] nics = NetworkInterface.GetAllNetworkInterfaces();
    Console.WriteLine("Interface information for {0}.{1}     ",
            computerProperties.HostName, computerProperties.DomainName);
    if (nics == null || nics.Length < 1)
    {
        Console.WriteLine("  No network interfaces found.");
        return;
    }

    Console.WriteLine("  Number of interfaces .................... : {0}", nics.Length);

    foreach (NetworkInterface adapter in nics)
    {
        IPInterfaceProperties properties = adapter.GetIPProperties();
        Console.WriteLine();
        Console.WriteLine(adapter.Description);
        Console.WriteLine(String.Empty.PadLeft(adapter.Description.Length, '='));
        Console.WriteLine("  Interface type .......................... : {0}", adapter.NetworkInterfaceType);
        Console.WriteLine("  Physical Address ........................ : {0}",
                    adapter.GetPhysicalAddress().ToString());
        Console.WriteLine("  Operational status ...................... : {0}",
            adapter.OperationalStatus);
        string versions = "";

        // Create a display string for the supported IP versions.
        if (adapter.Supports(NetworkInterfaceComponent.IPv4))
        {
            versions = "IPv4";
        }
        if (adapter.Supports(NetworkInterfaceComponent.IPv6))
        {
            if (versions.Length > 0)
            {
                versions += " ";
            }
            versions += "IPv6";
        }
        Console.WriteLine("  IP version .............................. : {0}", versions);
        //ShowIPAddresses(properties);

        // The following information is not useful for loopback adapters.
        if (adapter.NetworkInterfaceType == NetworkInterfaceType.Loopback)
        {
            continue;
        }
        Console.WriteLine("  DNS suffix .............................. : {0}",
            properties.DnsSuffix);

        string label;
        if (adapter.Supports(NetworkInterfaceComponent.IPv4))
        {
            IPv4InterfaceProperties ipv4 = properties.GetIPv4Properties();
            Console.WriteLine("  MTU...................................... : {0}", ipv4.Mtu);
            if (ipv4.UsesWins)
            {

                IPAddressCollection winsServers = properties.WinsServersAddresses;
                if (winsServers.Count > 0)
                {
                    label = "  WINS Servers ............................ :";
                    //ShowIPAddresses(label, winsServers);
                }
            }
        }

        Console.WriteLine("  DNS enabled ............................. : {0}",
            properties.IsDnsEnabled);
        Console.WriteLine("  Dynamically configured DNS .............. : {0}",
            properties.IsDynamicDnsEnabled);
        Console.WriteLine("  Receive Only ............................ : {0}",
            adapter.IsReceiveOnly);
        Console.WriteLine("  Multicast ............................... : {0}",
            adapter.SupportsMulticast);
    }
}
ManagementObjectSearcher myAudioObject = new ManagementObjectSearcher("select * from Win32_SoundDevice");

foreach (ManagementObject obj in myAudioObject.Get())
{
    Console.WriteLine("Name  -  " + obj["Name"]);
    Console.WriteLine("ProductName  -  " + obj["ProductName"]);
    Console.WriteLine("Availability  -  " + obj["Availability"]);
    Console.WriteLine("DeviceID  -  " + obj["DeviceID"]);
    Console.WriteLine("PowerManagementSupported  -  " + obj["PowerManagementSupported"]);
    Console.WriteLine("Status  -  " + obj["Status"]);
    Console.WriteLine("StatusInfo  -  " + obj["StatusInfo"]);
    Console.WriteLine(String.Empty.PadLeft(obj["ProductName"].ToString().Length, '='));
}
ManagementObjectSearcher myPrinterObject = new ManagementObjectSearcher("select * from Win32_Printer");

foreach (ManagementObject obj in myPrinterObject.Get())
{
    Console.WriteLine("Name  -  " + obj["Name"]);
    Console.WriteLine("Network  -  " + obj["Network"]);
    Console.WriteLine("Availability  -  " + obj["Availability"]);
    Console.WriteLine("Is default printer  -  " + obj["Default"]);
    Console.WriteLine("DeviceID  -  " + obj["DeviceID"]);
    Console.WriteLine("Status  -  " + obj["Status"]);
    
    Console.WriteLine(String.Empty.PadLeft(obj["Name"].ToString().Length, '='));
}
