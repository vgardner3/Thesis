//Automated email java
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import java.util.Properties;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // Email configuration
        final String senderEmail = "your_email@example.com";
        final String password = "your_email_password";
        final String receiverEmail = "recipient_email@example.com";

        // Create message
        Properties props = new Properties();
        props.put("mail.smtp.host", "smtp.example.com");
        props.put("mail.smtp.socketFactory.port", "465");
        props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.port", "465");

        Session session = Session.getDefaultInstance(props, new javax.mail.Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(senderEmail, password);
            }
        });

        try {
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(senderEmail));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(receiverEmail));
            message.setSubject("Automated Email Notification");
            
            String body = "Hello,\n\nThis is an automated email sent using Java.\n\nRegards,\n[Your Name]";
            message.setText(body);

            Transport.send(message);
            System.out.println("Email sent successfully!");

        } catch (MessagingException e) {
            System.out.println("Failed to send email. Error: " + e.getMessage());
        }

        // Simulate user registration (using console input for simplicity)
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your username: ");
        String username = scanner.nextLine();

        System.out.print("Enter your password: ");
        String userPassword = scanner.nextLine();

        System.out.print("Enter your security question: ");
        String securityQuestion = scanner.nextLine();

        System.out.print("Enter your security answer: ");
        String securityAnswer = scanner.nextLine();

        // Store user information (in real-world scenario, you would use a database)
        UserDatabase userDatabase = UserDatabase.getInstance();
        userDatabase.registerUser(username, userPassword, securityQuestion, securityAnswer);

        System.out.println("Registration successful!");
    }
}

// Simulated database to store user information
class UserDatabase {
    private static UserDatabase instance;
    // You would typically use a proper data structure or database connection here
    // For simplicity, I'm using a basic map to store user information
    private Map<String, UserInfo> database;

    private UserDatabase() {
        database = new HashMap<>();
    }

    public static UserDatabase getInstance() {
        if (instance == null) {
            instance = new UserDatabase();
        }
        return instance;
    }

    public void registerUser(String username, String password, String securityQuestion, String securityAnswer) {
        UserInfo userInfo = new UserInfo(username, password, securityQuestion, securityAnswer);
        database.put(username, userInfo);
    }
}

// User information class
class UserInfo {
    private String password;
    private String securityQuestion;
    private String securityAnswer;

    public UserInfo(String password, String securityQuestion, String securityAnswer) {
        this.password = password;
        this.securityQuestion = securityQuestion;
        this.securityAnswer = securityAnswer;
    }

    // Getters and setters if needed
}
