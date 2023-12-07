import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.awt.image.BufferedImage;

public class EnseniameApp {
    private JFrame frame;
    private JPanel menuPanel;
    private JButton abecedarioButton;
    private JButton familiaButton;
    private JButton saludosButton;
    private JButton backButton;
    private JButton backToMainButton;
    private EmptyBorder marginBorder;
    private JButton padreButton;
    private JButton madreButton;
    private JButton hermanoButton;
    private JButton hermanaButton;
    private JButton abueloButton;
    private JButton abuelaButton;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new EnseniameApp());
    }
    public EnseniameApp() {
        frame = new JFrame("ENSENIAME");
        frame.getContentPane().setBackground(new Color(12, 143, 143));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        showMain();
        frame.setVisible(true);

    }

    private void showMain() {
        frame.getContentPane().removeAll();
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
        // CREAR TEXTO DE BIENVENIDA
        JLabel bienvenida = new JLabel("BIENVENIDO A ENSENIAME");
        font = new Font("Arial", Font.PLAIN, 20);
        bienvenida.setFont(font);
        bienvenida.setForeground(Color.WHITE);
        marginBorder = new EmptyBorder(40, 0, 20, 0);
        bienvenida.setBorder(marginBorder);
        gbc.gridy = 2;
        frame.add(bienvenida, gbc);
        // CREAR BOTON DE ACEPTAR
        JButton botonAceptar = new JButton("ACEPTAR");
        botonAceptar.setBackground(Color.BLACK);
        botonAceptar.setForeground(Color.WHITE);
        gbc.gridy = 3;
        frame.add(botonAceptar, gbc);
        // Funcionalidad del nombre
        botonAceptar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nombre = campoNombre.getText();
                bienvenida.setText("BIENVENIDO A ENSENIAME " + nombre);
            }
        });

        // CREAR BOTON DE IR A MENU
        JButton botonMenu = new JButton("IR AL MENU");
        botonMenu.setBackground(Color.BLACK);
        botonMenu.setForeground(Color.WHITE);
        // Funcionalidad de IR A MENU
        botonMenu.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showMenu();
            }
        });
        gbc.gridy = 4;
        frame.add(botonMenu, gbc);
        frame.revalidate();
        frame.repaint();
    }

    private void showMenu() {
        frame.getContentPane().removeAll();
        frame.setLayout(new BorderLayout());
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
    
        backToMainButton = createButton("Volver"); // Se agrega el botón de vuelta a la pantalla principal
        menuPanel.add(backToMainButton); // Se agrega el botón de vuelta a la pantalla principal

        backButton = createButton("Volver");
        backButton.setVisible(false);

        // frame.add(welcomePanel, BorderLayout.NORTH);
        frame.add(menuPanel, BorderLayout.CENTER);

        frame.revalidate();
        frame.repaint();
    }

    private JButton createButton(String text) {
        JButton button = new JButton(text);
        button.setMaximumSize(new Dimension(60, 30)); // Establecer el tamaño máximo
        button.setPreferredSize(new Dimension(60, 30)); // Establecer el tamaño preferido
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
        } else if (e.getSource() == padreButton) {
            showFamiliaGif("PADRE", "img/Padres.gif");
        } else if (e.getSource() == madreButton) {
            showFamiliaGif("MADRE", "img/Madre.gif");
        } else if (e.getSource() == hermanoButton) {
            showFamiliaGif("HERMANO", "img/Hermano.gif");
        } else if (e.getSource() == hermanaButton) {
            showFamiliaGif("HERMANA", "img/Hermana.gif");
        } else if (e.getSource() == abueloButton) {
            showFamiliaGif("ABUELO", "img/Abuelo.gif");
        } else if (e.getSource() == abuelaButton) {
            showFamiliaGif("ABUELA", "img/Abuela.gif");
        } else if (e.getSource() == backToMainButton) {
            showMain();
        }

    }

    //////
    private void showSaludos() {
        // Mapa con los Saludos y Frases
        Map<String, String> validos = new HashMap<>();
        validos.put("hola", "img/Hola.gif");
        validos.put("buenos dias", "img/BuenosDias.gif");
        validos.put("buenas tardes", "img/BuenasTardes.gif");
        validos.put("buenas noches", "img/BuenasNoches.gif");
        validos.put("adios", "img/Adios.gif");
        validos.put("hasta pronto", "img/HastaManana.gif");
        validos.put("que tal", "img/Quetal.gif");
        validos.put("bien", "img/Bien.gif");
        validos.put("regular", "img/Regular.gif");
        validos.put("mal", "img/Mal.gif");
        validos.put("mi nombre", "img/MiNombre.gif");
        validos.put("yo soy sordo", "img/Sordo.gif");

        frame.getContentPane().removeAll();
        frame.setLayout(new BorderLayout());
        JPanel saludosPanel = new JPanel();
        saludosPanel.setLayout(new GridLayout(4, 1, 20, 20)); // Se agrega un espacio para el botón de vuelta
        saludosPanel.setBackground(new Color(12, 143, 143)); // Cambiar el color de fondo a amarillo

        JTextField buscador = new JTextField("INGRESE SALUDO O FRASE A BUSCAR"); // Crear el campo de texto
        // Boton para buscar
        JButton botonBuscar = new JButton("BUSCAR");
        botonBuscar.setBackground(Color.BLACK);
        botonBuscar.setForeground(Color.WHITE);
        // Funcionalidad de IR A MENU
        botonBuscar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String busqueda = buscador.getText().strip().toLowerCase();
                if (validos.containsKey(busqueda)) {
                    showSaludoGif(busqueda.toUpperCase(), validos.get(busqueda));
                } else {
                    JOptionPane.showMessageDialog(frame, "Aun no conozco ese saludo o frase");
                }
            }
        });
        saludosPanel.add(buscador); // Agregar el campo de texto al panel
        saludosPanel.add(botonBuscar);
        saludosPanel.add(backButton); // Se agrega el botón de vuelta a la sección

        backButton.setVisible(true); // Se muestra el botón de vuelta

        frame.getContentPane().add(saludosPanel, BorderLayout.CENTER);
        frame.revalidate();
        frame.repaint();
    }

    private void showSaludoGif(String title, String gif) {
        frame.getContentPane().removeAll();
        frame.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        // Titulo
        JLabel bienvenida = new JLabel(title);
        Font font = new Font("Arial", Font.PLAIN, 20);
        bienvenida.setFont(font);
        bienvenida.setForeground(Color.WHITE);
        marginBorder = new EmptyBorder(40, 0, 40, 0);
        bienvenida.setBorder(marginBorder);
        gbc.gridx = 0;
        gbc.gridy = 0;
        frame.add(bienvenida, gbc);
        // GIF
        ImageIcon gifIcon = new ImageIcon(gif);
        JLabel gifLabel = new JLabel(gifIcon);
        gbc.gridy = 1;
        frame.add(gifLabel, gbc);
        // BOTON DE VOLVER
        JButton botonVolverFamilia = new JButton("VOLVER");
        botonVolverFamilia.setBackground(Color.BLACK);
        botonVolverFamilia.setForeground(Color.WHITE);
        // Funcionalidad de IR A MENU
        botonVolverFamilia.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showSaludos();
            }
        });
        gbc.gridy = 2;
        frame.add(botonVolverFamilia, gbc);
        frame.revalidate();
        frame.repaint();
    }


    private void showFamilia() {
        frame.getContentPane().removeAll();
        frame.setLayout(new BorderLayout());
        JPanel familiaPanel = new JPanel();
        familiaPanel.setLayout(new GridLayout(4, 1, 20, 20)); // Se agrega un espacio para el botón de vuelta
    
        padreButton = createButton("Padre");
        madreButton = createButton("Madre");
        hermanoButton = createButton("Hermano");
        hermanaButton = createButton("Hermana");
        abueloButton = createButton("Abuelo");
        abuelaButton = createButton("Abuela");
    
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

        frame.getContentPane().add(familiaPanel, BorderLayout.CENTER);
        frame.revalidate();
        frame.repaint();
    }


    private void showFamiliaGif(String title, String gif) {
        frame.getContentPane().removeAll();
        frame.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        // Titulo
        JLabel bienvenida = new JLabel(title);
        Font font = new Font("Arial", Font.PLAIN, 20);
        bienvenida.setFont(font);
        bienvenida.setForeground(Color.WHITE);
        marginBorder = new EmptyBorder(40, 0, 40, 0);
        bienvenida.setBorder(marginBorder);
        gbc.gridx = 0;
        gbc.gridy = 0;
        frame.add(bienvenida, gbc);
        // GIF
        ImageIcon gifIcon = new ImageIcon(gif);
        JLabel gifLabel = new JLabel(gifIcon);
        gbc.gridy = 1;
        frame.add(gifLabel, gbc);
        // BOTON DE VOLVER
        JButton botonVolverFamilia = new JButton("VOLVER");
        botonVolverFamilia.setBackground(Color.BLACK);
        botonVolverFamilia.setForeground(Color.WHITE);
        // Funcionalidad de IR A MENU
        botonVolverFamilia.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showFamilia();
            }
        });
        gbc.gridy = 2;
        frame.add(botonVolverFamilia, gbc);
        frame.revalidate();
        frame.repaint();
    }

    private void showAbecedario() {
    frame.getContentPane().removeAll();

    JPanel abecedarioPanel = new JPanel();
    abecedarioPanel.setLayout(new GridLayout(4, 7, 20, 20)); // Se agrega un espacio para el botón de vuelta

    // Crea los botones con las imágenes correspondientes
    JButton aButton = createButtonWithImage("A", "img/A.png");
    JButton bButton = createButtonWithImage("B", "img/B.png");
    JButton cButton = createButtonWithImage("C", "img/C.png");
    JButton dButton = createButtonWithImage("D", "img/D.png");
    JButton eButton = createButtonWithImage("E", "img/E.png");
    JButton fButton = createButtonWithImage("F", "img/F.png");
    JButton gButton = createButtonWithImage("G", "img/G.png");
    JButton hButton = createButtonWithImage("H", "img/H.png");
    JButton iButton = createButtonWithImage("I", "img/I.png");
    JButton jButton = createButtonWithImage("J", "img/J.png");
    JButton kButton = createButtonWithImage("K", "img/K.png");
    JButton lButton = createButtonWithImage("L", "img/L.png");
    JButton mButton = createButtonWithImage("M", "img/M.png");
    JButton nButton = createButtonWithImage("N", "img/N.png");
    JButton oButton = createButtonWithImage("O", "img/O.png");
    JButton pButton = createButtonWithImage("P", "img/P.png");
    JButton qButton = createButtonWithImage("Q", "img/Q.png");
    JButton rButton = createButtonWithImage("R", "img/R.png");
    JButton sButton = createButtonWithImage("S", "img/S.png");
    JButton tButton = createButtonWithImage("T", "img/T.png");
    JButton uButton = createButtonWithImage("U", "img/U.png");
    JButton vButton = createButtonWithImage("V", "img/V.png");
    JButton wButton = createButtonWithImage("W", "img/W.png");
    JButton xButton = createButtonWithImage("X", "img/X.png");
    JButton yButton = createButtonWithImage("Y", "img/Y.png");
    JButton zButton = createButtonWithImage("Z", "img/Z.png");

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
