using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ProjetV1
{
    public partial class frmAccueil : Form
    {
        public frmAccueil()
        {
            InitializeComponent();
        }

        #region None style sizeable
        private PictureBox title = new PictureBox();
        private bool drag = false;
        private Point startPoint = new Point(0, 0);
        private void btnClose_MouseClick(object sender, MouseEventArgs e)
        {
            if ((sender as Button).Text == "X") this.Close();
            else if ((sender as Button).Text == "+" || (sender as Button).Text == "-")
            {
                if ((sender as Button).Text == "+")
                {
                    this.WindowState = FormWindowState.Maximized;
                    (sender as Button).Text = "-";
                    this.title.Width = this.Width;
                }
                else
                {
                    this.WindowState = FormWindowState.Normal;
                    (sender as Button).Text = "+";
                }
            }
            else this.WindowState = FormWindowState.Minimized;
        }
        void Title_MouseUp(object sender, MouseEventArgs e)
        {
            this.drag = false;
        }
        void Title_MouseDown(object sender, MouseEventArgs e)
        {
            this.startPoint = e.Location;
            this.drag = true;
        }
        void Title_MouseMove(object sender, MouseEventArgs e)
        {
            if (this.drag)
            { // if we should be dragging it, we need to figure out some movement
                Point p1 = new Point(e.X, e.Y);
                Point p2 = this.PointToScreen(p1);
                Point p3 = new Point(p2.X - this.startPoint.X, p2.Y - this.startPoint.Y);
                this.Location = p3;
            }
        }
        private bool resizing = false;
        private Point last = new Point(0, 0);
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!resizing)
            {
                bool resize_x = e.X > (this.Width - 8);
                bool resize_y = e.Y > (this.Height - 8);
                if (resize_x && resize_y) this.Cursor = Cursors.SizeNWSE;
                else if (resize_x) this.Cursor = Cursors.SizeWE;
                else if (resize_y) this.Cursor = Cursors.SizeNS;
                else this.Cursor = Cursors.Default;
            }
            else
            {
                int w = this.Size.Width;
                int h = this.Size.Height;
                if (this.Cursor.Equals(Cursors.SizeNWSE))
                    this.Size = new Size(w + (e.Location.X - this.last.X), h + (e.Location.Y - this.last.Y));
                else if (this.Cursor.Equals(Cursors.SizeWE))
                    this.Size = new Size(w + (e.Location.X - this.last.X), h);
                else if (this.Cursor.Equals(Cursors.SizeNS))
                    this.Size = new Size(w, h + (e.Location.Y - this.last.Y));
                this.last = e.Location;
            }
        }
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            this.resizing = true;
            this.last = e.Location;
        }
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            this.resizing = false;
        }
        protected override CreateParams CreateParams
        {
            get
            {
                CreateParams cp = base.CreateParams;
                cp.Style |= 0x40000;
                return cp;
            }
        }
        #endregion

    }
}
