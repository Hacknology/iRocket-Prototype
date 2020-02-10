using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using GMap.NET;
using GMap.NET.MapProviders;
using GMap.NET.WindowsForms;
using GMap.NET.WindowsForms.Markers;
using GMap.NET.WindowsForms.ToolTips;
using GMap.NET.MapProviders;
/*
 İSTANBUL TEKNİK ÜNİVERSİTESİ SAV-TEK KULÜBÜ
 TEKNOFEST 2020 GAZİANTEP
 */
namespace iRocketv0._2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Test");
            /*
             He's flying higher... King of the sky
             He's flying too fast n' he's flying too high
             
             */
        }

        private void map_Load(object sender, EventArgs e)
        {

        }

        public void Form1_Load(object sender, EventArgs e)
        {
            GMaps.Instance.Mode = AccessMode.ServerAndCache;
            map.CacheLocation = @"C:\Users\Casper\Desktop\mapcaches";

            map.DragButton = MouseButtons.Left;
            map.MapProvider = GMapProviders.GoogleMap;
            double lat = Convert.ToDouble(37.06622);
            double langt = Convert.ToDouble(37.38332);
            map.Position = new PointLatLng(lat, langt);
            map.MinZoom = 0;
            map.MaxZoom = 18;
            map.Zoom = 12;

            

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "/C py C:\\Users\\Casper\\source\\repos\\iRocketv0.2\\iRocketv0.2\\python-imports\\iRocket.py";
            process.StartInfo = startInfo;
            process.Start();
        }
    }
}
