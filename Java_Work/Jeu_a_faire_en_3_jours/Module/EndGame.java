package Module;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.block.BlockBorder;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.chart.title.TextTitle;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.*;
import javax.swing.BorderFactory;
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Font;

import java.nio.charset.StandardCharsets;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class EndGame extends JPanel {
    JLabel conclusion = new JLabel();
    public EndGame(Calcule cal){
        EventQueue.invokeLater(() -> {
            var ex = new Graph(cal);
            ex.setVisible(true);
        });
        if (cal.hextra.size()>60){
            String txt = "Tu as gagné, tu peux maintenant avoir les compétences pour faire ton propre pays."; 
            byte[] biteTxt = txt.getBytes();
            conclusion.setText(new String(biteTxt, StandardCharsets.UTF_8));
        }
        else {
            String txt = "Tu as perdu, mais c'est pas grave, tu pourras te reconvertir et trouvé une autre voie."; 
            byte[] biteTxt = txt.getBytes();
            conclusion.setText(new String(biteTxt, StandardCharsets.UTF_8));
        }
        add(conclusion);
    }
}

class Graph extends JPanel {
    public Graph(Calcule cal){
        XYDataset dataset;
        if (cal.isconso) dataset = createDataset(cal.conshistory);
        else dataset = createDataset(cal.prodhistory);
        JFreeChart chart = createChart(dataset);

        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));
        chartPanel.setBackground(Color.white);
        add(chartPanel);
    }

    public XYDataset createDataset(List<Integer> res) {
        var series = new XYSeries("Argent");
        int i = 0;
        for (int d : res){
            series.add(i++, d);
        }
        var dataset = new XYSeriesCollection();
        dataset.addSeries(series);
        return dataset;
    }

    public JFreeChart createChart(XYDataset dataset) {
        JFreeChart chart = ChartFactory.createXYLineChart(
            "Résultat de la simulation",
            "u.a.","Temps en jour", dataset, PlotOrientation.VERTICAL,
            true, true, false);

        XYPlot plot = chart.getXYPlot();

        var renderer = new XYLineAndShapeRenderer();
        renderer.setSeriesPaint(0, Color.RED);
        renderer.setSeriesStroke(0, new BasicStroke(2.0f));

        plot.setRenderer(renderer);
        plot.setBackgroundPaint(Color.white);

        plot.setRangeGridlinesVisible(true);
        plot.setRangeGridlinePaint(Color.BLACK);

        plot.setDomainGridlinesVisible(true);
        plot.setDomainGridlinePaint(Color.BLACK);

        chart.getLegend().setFrame(BlockBorder.NONE);
        chart.setTitle(new TextTitle("Average Salary per Age",
                        new Font("Serif", java.awt.Font.BOLD, 18))
        );

        return chart;
    }
}