using System.Net.NetworkInformation;  
using system;

private static bool IsMachineUp(string hostName)
{
    bool retVal = false;
    try
    {
        Ping pingSender = new Ping();
        PingOptions options = new PingOptions();
        options.DontFragment = true;
        string data = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        byte[] buffer = Encoding.ASCII.GetBytes(data);
        int timeout = 120;
 
        PingReply reply = pingSender.Send(hostName, timeout, buffer, options);
        if (reply.Status == IPStatus.Success)
        {
            retVal = true;
        }
    }
    catch (Exception ex)
    {
        retVal = false;
        Console.WriteLine(ex.Message);
    }
    return retVal;
}
