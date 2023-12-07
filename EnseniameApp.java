import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.awt.image.BufferedImage;

public class EnseniameApp {
    private JFrame frame;
    private JPanel welcomePanel;
    private JLabel welcomeLabel;
    private JPanel menuPanel;
    private JButton abecedarioButton;
    private JButton familiaButton;
    private JButton saludosButton;
    private JButton backButton; // Botón de vuelta
    private EmptyBorder marginBorder;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new EnseniameApp());
    }
    public EnseniameApp() {
        frame = new JFrame("ENSENIAME");
        frame.getContentPane().setBackground(new Color(12, 143, 143));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        // CREAR LOGO
        // Cargar la imagen
        BufferedImage imagen = null;
        try {
            imagen = ImageIO.read(new File("img/logo.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        ImageIcon imageIcon = new ImageIcon(imagen);
        Image scaledImage = imageIcon.getImage().getScaledInstance(150, 150, Image.SCALE_SMOOTH);
        ImageIcon scaledIcon = new ImageIcon(scaledImage);
        JLabel imageLabel = new JLabel(scaledIcon);
        gbc.gridx = 0;
        gbc.gridy = 0;
        marginBorder = new EmptyBorder(0, 0, 40, 0);
        imageLabel.setBorder(marginBorder);
        frame.add(imageLabel, gbc);
        // CREAR EL CAMPO DE TEXTO
        JTextField campoNombre = new JTextField("INGRESE SU NOMBRE");
        Font font = new Font("Arial", Font.PLAIN, 20);
        campoNombre.setFont(font);
        gbc.gridy = 1;
        frame.add(campoNombre, gbc);

        frame.setVisible(true);

    }

    private void showMenuPanel() {
        menuPanel = new JPanel();
        menuPanel.setBackground(new Color(12, 143, 143));
        menuPanel.setLayout(new GridLayout(4, 1, 20, 20)); // Se agrega un espacio para el botón de vuelta
    
        abecedarioButton = createButton("Abecedario");
        familiaButton = createButton("Familia");
        saludosButton = createButton("Saludos");
    
        // Cambiar el color de fondo de los botones en el menú
        abecedarioButton.setBackground(new Color(102, 204, 204));
        familiaButton.setBackground(new Color(102, 204, 204));
        saludosButton.setBackground(new Color(102, 204, 204));
    
        // Cambiar el tamaño de los botones en el menú
        abecedarioButton.setPreferredSize(new Dimension(200, 70));
        familiaButton.setPreferredSize(new Dimension(200, 70));
        saludosButton.setPreferredSize(new Dimension(200, 70));
    
        menuPanel.add(abecedarioButton);
        menuPanel.add(familiaButton);
        menuPanel.add(saludosButton);
    
        backButton = createButton("Volver"); // Se agrega el botón de vuelta
        backButton.setVisible(false); // Se oculta inicialmente
    
        menuPanel.add(backButton); // Se agrega el botón de vuelta al menú

        frame.add(welcomePanel, BorderLayout.NORTH);
        frame.add(menuPanel, BorderLayout.CENTER);
    }

    private JButton createButton(String text) {
        JButton button = new JButton(text);
        button.setMaximumSize(new Dimension(10, 10)); // Establecer el tamaño máximo
        button.setPreferredSize(new Dimension(10, 10)); // Establecer el tamaño preferido
        button.addActionListener(e -> handleButtonClick(e));
        return button;
    }
    private void handleButtonClick(ActionEvent e) {
        if (e.getSource() == abecedarioButton) {
            showAbecedario();
        } else if (e.getSource() == familiaButton) {
            showFamilia();
        } else if (e.getSource() == saludosButton) {
            showSaludos();
        } else if (e.getSource() == backButton) { // Manejo del botón de vuelta
            showMenu();
        }
    }

    private void showMenu() {
        frame.getContentPane().removeAll();
        frame.getContentPane().add(welcomePanel, BorderLayout.NORTH);
        frame.getContentPane().add(menuPanel, BorderLayout.CENTER);
        backButton.setVisible(false); // Se oculta el botón de vuelta en el menú principal
        frame.revalidate();
        frame.repaint();
    }

    //////
    private void showSaludos() {
        frame.getContentPane().removeAll();
    
        JPanel saludosPanel = new JPanel();
        saludosPanel.setLayout(new GridLayout(4, 1, 20, 20)); // Se agrega un espacio para el botón de vuelta
        saludosPanel.setBackground(new Color(12, 143, 143)); // Cambiar el color de fondo a amarillo
    
        JTextField textField = new JTextField(); // Crear el campo de texto
    
        saludosPanel.add(textField); // Agregar el campo de texto al panel
        saludosPanel.add(backButton); // Se agrega el botón de vuelta a la sección
    
        backButton.setVisible(true); // Se muestra el botón de vuelta
    
        frame.getContentPane().add(saludosPanel, BorderLayout.CENTER);
        frame.revalidate();
        frame.repaint();
    }
        


    /////


    private void showFamilia() {
        frame.getContentPane().removeAll();
    
        JPanel familiaPanel = new JPanel();
        familiaPanel.setLayout(new GridLayout(4, 1, 20, 20)); // Se agrega un espacio para el botón de vuelta
    
        JButton padreButton = createButton("Padre");
        JButton madreButton = createButton("Madre");
        JButton hermanoButton = createButton("Hermano");
        JButton hermanaButton = createButton("Hermana");
        JButton abueloButton = createButton("Abuelo");
        JButton abuelaButton = createButton("Abuela");
    
        familiaPanel.setBackground(new Color(12, 143, 143)); // Cambiar el color de fondo a amarillo
    
        // Cambiar el color de fondo de los botones
        padreButton.setBackground(new Color(102, 204, 204));
        madreButton.setBackground(new Color(102, 204, 204));
        hermanoButton.setBackground(new Color(102, 204, 204));
        hermanaButton.setBackground(new Color(102, 204, 204));
        abueloButton.setBackground(new Color(102, 204, 204));
        abuelaButton.setBackground(new Color(102, 204, 204));
        backButton.setBackground(new Color(102, 204, 204));
    
        familiaPanel.add(padreButton);
        familiaPanel.add(madreButton);
        familiaPanel.add(hermanoButton);
        familiaPanel.add(hermanaButton);
        familiaPanel.add(abueloButton);
        familiaPanel.add(abuelaButton);
    
        familiaPanel.add(backButton); // Se agrega el botón de vuelta a la sección
    
        backButton.setVisible(true); // Se muestra el botón de vuelta
    
        // Agregar ActionListener al botón para mostrar el GIF del Padre
        padreButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // mostrarGif("src/Papá.gif");
            }
        });
    
        // Agregar ActionListener al botón para mostrar el GIF de la Madre
        madreButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // mostrarGif("src/Ma.gif");
            }
        });
    
        // Agregar ActionListener al botón para mostrar el GIF del Hermano
        hermanoButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // mostrarGif("src/Hermano.gif");
            }
        });
    
        // Agregar ActionListener al botón para mostrar el GIF de la Hermana
        hermanaButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // mostrarGif("src/Hermana.gif");
            }
        });
    
        // Agregar ActionListener al botón para mostrar el GIF del Abuelo
        abueloButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // mostrarGif("src/Abuelo.gif");
            }
        });
    
        // Agregar ActionListener al botón para mostrar el GIF de la Abuela
        abuelaButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // mostrarGif("src/Abuela.gif");
            }
        });
    
        frame.getContentPane().add(familiaPanel, BorderLayout.CENTER);
        frame.revalidate();
        frame.repaint();
    }


    private void showAbecedario() {
    frame.getContentPane().removeAll();

    JPanel abecedarioPanel = new JPanel();
    abecedarioPanel.setLayout(new GridLayout(4, 7, 20, 20)); // Se agrega un espacio para el botón de vuelta

    // Crea los botones con las imágenes correspondientes
    JButton aButton = createButtonWithImage("A", "src/letraA.png");
    JButton bButton = createButtonWithImage("B", "src/letraB.png");
    JButton cButton = createButtonWithImage("C", "src/letraC.png");
    JButton dButton = createButtonWithImage("D", "src/letraD.png");
    JButton eButton = createButtonWithImage("E", "src/letraE.png");
    JButton fButton = createButtonWithImage("F", "src/letraF.png");
    JButton gButton = createButtonWithImage("G", "src/letraG.png");
    JButton hButton = createButtonWithImage("H", "src/letraH.png");
    JButton iButton = createButtonWithImage("I", "src/letraI.png");
    JButton jButton = createButtonWithImage("J", "src/letraJ.png");
    JButton kButton = createButtonWithImage("K", "src/letraK.png");
    JButton lButton = createButtonWithImage("L", "src/letraL.png");
    JButton mButton = createButtonWithImage("M", "src/letraM.png");
    JButton nButton = createButtonWithImage("N", "src/letraN.png");
    JButton oButton = createButtonWithImage("O", "src/letraO.png");
    JButton pButton = createButtonWithImage("P", "src/letraP.png");
    JButton qButton = createButtonWithImage("Q", "src/letraQ.png");
    JButton rButton = createButtonWithImage("R", "src/letraR.png");
    JButton sButton = createButtonWithImage("S", "src/letraS.png");
    JButton tButton = createButtonWithImage("T", "src/letraT.png");
    JButton uButton = createButtonWithImage("U", "src/letraU.png");
    JButton vButton = createButtonWithImage("V", "src/letraV.png");
    JButton wButton = createButtonWithImage("W", "src/letraW.png");
    JButton xButton = createButtonWithImage("X", "src/letraX.png");
    JButton yButton = createButtonWithImage("Y", "src/letraY.png");
    JButton zButton = createButtonWithImage("Z", "src/letraZ.png");

    abecedarioPanel.add(aButton);
    abecedarioPanel.add(bButton);
    abecedarioPanel.add(cButton);
    abecedarioPanel.add(dButton);
    abecedarioPanel.add(eButton);
    abecedarioPanel.add(fButton);
    abecedarioPanel.add(gButton);
    abecedarioPanel.add(hButton);
    abecedarioPanel.add(iButton);
    abecedarioPanel.add(jButton);
    abecedarioPanel.add(kButton);
    abecedarioPanel.add(lButton);
    abecedarioPanel.add(mButton);
    abecedarioPanel.add(nButton);
    abecedarioPanel.add(oButton);
    abecedarioPanel.add(pButton);
    abecedarioPanel.add(qButton);
    abecedarioPanel.add(rButton);
    abecedarioPanel.add(sButton);
    abecedarioPanel.add(tButton);
    abecedarioPanel.add(uButton);
    abecedarioPanel.add(vButton);
    abecedarioPanel.add(wButton);
    abecedarioPanel.add(xButton);
    abecedarioPanel.add(yButton);
    abecedarioPanel.add(zButton);

    abecedarioPanel.add(backButton); // Se agrega el botón de vuelta a la sección

    abecedarioPanel.setBackground(Color.gray);

    backButton.setVisible(true); // Se muestra el botón de vuelta
    frame.getContentPane().add(abecedarioPanel, BorderLayout.CENTER);
    frame.revalidate();
    frame.repaint();
}

    // Método para crear un botón con una imagen
    private JButton createButtonWithImage(String buttonText, String imagePath) {
    ImageIcon icon = new ImageIcon(imagePath);
    Image image = icon.getImage();
    
    // Ajusta el tamaño de la imagen
    int width = 90; // Anchura deseada
    int height = 90; // Altura deseada
    Image scaledImage = image.getScaledInstance(width, height, Image.SCALE_SMOOTH);
    
    ImageIcon scaledIcon = new ImageIcon(scaledImage);
    JButton button = new JButton(buttonText, scaledIcon);
    button.setVerticalTextPosition(SwingConstants.BOTTOM);
    button.setHorizontalTextPosition(SwingConstants.CENTER);
    return button;
    }
}

class LogoPanel extends JPanel {
    private BufferedImage image;

    public LogoPanel() {
        try {
            // Load the image from a file
            image = ImageIO.read(new File("img/logo.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Draw the image at a specific (x, y) position
        int x = 50; // Adjust the x-coordinate as needed
        int y = 20; // Adjust the y-coordinate as needed

        g.drawImage(image, x, y, this);
    }
}