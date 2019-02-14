using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO.Ports;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace UDP_to_Serial
{
    public partial class Form1 : Form
    {
        UdpClient Client = new UdpClient(11001);
        public string data = "";
        System.IO.StreamReader in_file;
        Timer myTimer = new System.Windows.Forms.Timer();
        
        

        public Form1()
        {
            InitializeComponent();
            configrations();
        }

        public void configrations()
        {
            //to repeat serial func
            //myTimer.Tick += new EventHandler(send_data);
            //myTimer.Interval = 1000;

            //COM port information
            string[] ports = SerialPort.GetPortNames();
            cboPort.Items.AddRange(ports);

            cboPort.SelectedIndex = 0; //SelectedIndex = 0 -> 콤보박스의 첫번째 요소, SelectedIndex = 0 -> 콤보박스의 두번째 요소

            Close.Enabled = false;
            serialPort1.PortName = cboPort.Text;
            serialPort1.BaudRate = 115200;
            serialPort1.DataBits = 8;
            serialPort1.Parity = System.IO.Ports.Parity.None;
            serialPort1.StopBits = System.IO.Ports.StopBits.One;
        }

        //not working...
        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        
        private void Port_Click(object sender, EventArgs e)
        {
           
        }

        /* UDP data*/

        void recv(IAsyncResult res)
        {
            IPEndPoint RemoteIP = new IPEndPoint(IPAddress.Any, 11000);
            byte[] received = Client.EndReceive(res, ref RemoteIP);
            data = Encoding.ASCII.GetString(received);

            this.Invoke(new MethodInvoker(delegate
            {
                UDPdata.Text += "\nReceived data: " + data + Environment.NewLine;
                if (serialPort1.IsOpen)
                {

                    serialPort1.Write(data.Replace("\\n", Environment.NewLine)); //Write(data+Environmnet.NewLine) -> 225 출력 == \n 의 아스키코드 값
                    serialMessage.Text += data + Environment.NewLine;
                    //serialMessage.Clear();
                }
            }));

            Client.BeginReceive(new AsyncCallback(recv), null);
        }

        private void UDPrecv_Click(object sender, EventArgs e)
        {
            

            try
            {
                Client.BeginReceive(new AsyncCallback(recv), null);
            }
            catch (Exception ex)
            {
                UDPdata.Text += ex.Message.ToString();
            }
        }

        /* Serial Communication */

        private void cboPort_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Open_Click(object sender, EventArgs e)
        {

            Open.Enabled = false;
            Close.Enabled = true;
            try
            {
 
                serialPort1.Open();
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message, "Message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void Send_Click(object sender, EventArgs e)
        {
           //myTimer.Enabled = true;
           //myTimer.Start();
        
        }

        /*private void send_data(object sender, EventArgs e)
        {
            try
            {
                if (serialPort1.IsOpen)
                {
                    
                    serialPort1.WriteLine(data + Environment.NewLine);
                    serialMessage.Text += data+Environment.NewLine;
                    //serialMessage.Clear();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }*/

        private void Close_Click(object sender, EventArgs e)
        {
            Open.Enabled = true;
            Close.Enabled = false;
            try
            {
                
                serialPort1.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void Form1_Load_1(object sender, EventArgs e)
        {

        }
    }
}
