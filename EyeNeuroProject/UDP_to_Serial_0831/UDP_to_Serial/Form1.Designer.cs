namespace UDP_to_Serial
{
    partial class Form1
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.cboPort = new System.Windows.Forms.ComboBox();
            this.Port = new System.Windows.Forms.Label();
            this.Open = new System.Windows.Forms.Button();
            this.Close = new System.Windows.Forms.Button();
            this.UDPdata = new System.Windows.Forms.TextBox();
            this.serialMessage = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.UDPrecv = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.Send = new System.Windows.Forms.Button();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // cboPort
            // 
            this.cboPort.FormattingEnabled = true;
            this.cboPort.Location = new System.Drawing.Point(62, 31);
            this.cboPort.Name = "cboPort";
            this.cboPort.Size = new System.Drawing.Size(121, 20);
            this.cboPort.TabIndex = 0;
            this.cboPort.SelectedIndexChanged += new System.EventHandler(this.cboPort_SelectedIndexChanged);
            // 
            // Port
            // 
            this.Port.AutoSize = true;
            this.Port.Location = new System.Drawing.Point(21, 34);
            this.Port.Name = "Port";
            this.Port.Size = new System.Drawing.Size(41, 12);
            this.Port.TabIndex = 1;
            this.Port.Text = "Port: ";
            this.Port.Click += new System.EventHandler(this.Port_Click);
            // 
            // Open
            // 
            this.Open.Location = new System.Drawing.Point(205, 31);
            this.Open.Name = "Open";
            this.Open.Size = new System.Drawing.Size(75, 23);
            this.Open.TabIndex = 2;
            this.Open.Text = "Open";
            this.Open.UseVisualStyleBackColor = true;
            this.Open.Click += new System.EventHandler(this.Open_Click);
            // 
            // Close
            // 
            this.Close.Location = new System.Drawing.Point(298, 31);
            this.Close.Name = "Close";
            this.Close.Size = new System.Drawing.Size(75, 23);
            this.Close.TabIndex = 3;
            this.Close.Text = "Close";
            this.Close.UseVisualStyleBackColor = true;
            this.Close.Click += new System.EventHandler(this.Close_Click);
            // 
            // UDPdata
            // 
            this.UDPdata.Location = new System.Drawing.Point(18, 50);
            this.UDPdata.Multiline = true;
            this.UDPdata.Name = "UDPdata";
            this.UDPdata.Size = new System.Drawing.Size(282, 336);
            this.UDPdata.TabIndex = 4;
            // 
            // serialMessage
            // 
            this.serialMessage.Location = new System.Drawing.Point(23, 169);
            this.serialMessage.Multiline = true;
            this.serialMessage.Name = "serialMessage";
            this.serialMessage.Size = new System.Drawing.Size(523, 180);
            this.serialMessage.TabIndex = 4;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.UDPrecv);
            this.groupBox1.Controls.Add(this.UDPdata);
            this.groupBox1.Font = new System.Drawing.Font("굴림", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.groupBox1.Location = new System.Drawing.Point(603, 28);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(322, 410);
            this.groupBox1.TabIndex = 6;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Data From UDP";
            // 
            // UDPrecv
            // 
            this.UDPrecv.Location = new System.Drawing.Point(18, 21);
            this.UDPrecv.Name = "UDPrecv";
            this.UDPrecv.Size = new System.Drawing.Size(91, 23);
            this.UDPrecv.TabIndex = 5;
            this.UDPrecv.Text = "Start Recv";
            this.UDPrecv.UseVisualStyleBackColor = true;
            this.UDPrecv.Click += new System.EventHandler(this.UDPrecv_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.cboPort);
            this.groupBox2.Controls.Add(this.Port);
            this.groupBox2.Controls.Add(this.serialMessage);
            this.groupBox2.Controls.Add(this.Send);
            this.groupBox2.Controls.Add(this.Open);
            this.groupBox2.Controls.Add(this.Close);
            this.groupBox2.Font = new System.Drawing.Font("굴림", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.groupBox2.Location = new System.Drawing.Point(26, 28);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(558, 366);
            this.groupBox2.TabIndex = 7;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Serial Communication";
            this.groupBox2.Enter += new System.EventHandler(this.groupBox2_Enter);
            // 
            // Send
            // 
            this.Send.Location = new System.Drawing.Point(399, 31);
            this.Send.Name = "Send";
            this.Send.Size = new System.Drawing.Size(75, 23);
            this.Send.TabIndex = 5;
            this.Send.Text = "Send";
            this.Send.UseVisualStyleBackColor = true;
            this.Send.Click += new System.EventHandler(this.Send_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(963, 450);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load_1);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ComboBox cboPort;
        private System.Windows.Forms.Label Port;
        private System.Windows.Forms.Button Open;
        private System.Windows.Forms.Button Close;
        private System.Windows.Forms.TextBox UDPdata;
        private System.Windows.Forms.TextBox serialMessage;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button Send;
        private System.Windows.Forms.Button UDPrecv;
        private System.IO.Ports.SerialPort serialPort1;
    }
}

