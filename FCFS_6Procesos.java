import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

class Proceso {
    int id, rafaga;

    public Proceso(int id, int rafaga) {
        this.id = id;
        this.rafaga = rafaga;
    }
}

class GanttPanel extends JPanel {

    java.util.List<Integer> timeline = new ArrayList<>();
    int cellW = 40, cellH = 40;
    int startX = 120, startY = 50;

    public void addStep(int pid) {
        timeline.add(pid);
        repaint();
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Etiquetas procesos
        for (int i = 0; i < 6; i++) {
            g.drawString("P" + (i+1), 80, startY + i*cellH + 25);
        }

        // Dibujar timeline
        for (int t = 0; t < timeline.size(); t++) {
            int pid = timeline.get(t);

            int x = startX + t * cellW;
            int y = startY + (pid - 1) * cellH;

            g.setColor(Color.GREEN);
            g.fillRect(x, y, cellW, cellH);

            g.setColor(Color.BLACK);
            g.drawString("P"+pid, x+10, y+25);

            g.drawString("t"+t, x+10,
                startY + 6*cellH + 20);
        }
    }
}

public class FCFS_6Procesos {

    public static void main(String[] args) {

        JFrame frame = new JFrame("FCFS 6 Procesos");
        GanttPanel panel = new GanttPanel();

        frame.add(panel);
        frame.setSize(1200, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        new Thread(() -> simular(panel)).start();
    }

    static void simular(GanttPanel panel) {

        Random r = new Random();

        Queue<Proceso> cola = new LinkedList<>();

        for (int i = 1; i <= 6; i++) {
            cola.add(new Proceso(i, r.nextInt(5) + 2));
        }

        while (!cola.isEmpty()) {
            Proceso p = cola.poll();

            for (int i = 0; i < p.rafaga; i++) {
                panel.addStep(p.id);

                try { Thread.sleep(500); } catch(Exception e){}
            }
        }
    }
}