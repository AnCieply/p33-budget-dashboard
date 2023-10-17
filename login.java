import java.util.ArrayList;
import java.util.Scanner;

public class login {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ArrayList<String> usernames = new ArrayList<>();
        ArrayList<String> passwords = new ArrayList<>();

        usernames.add("icieply");
        usernames.add("sdawood1");
        usernames.add("ahasan18");
        usernames.add("wleung1");
        usernames.add("ktran20");
        usernames.add("ntrivedi2");

        passwords.add("Password1");
        passwords.add("Password2");
        passwords.add("Password3");
        passwords.add("Password4");
        passwords.add("Password5");
        passwords.add("Password6");

        boolean check = false;

        while (!check) {
            System.out.println("\t\t\t\t\t\t\t\tPlease enter your username or type 'new' to create a new account\n");
            String enteredUsername = scanner.next();

            if (enteredUsername.equals("new")) {
                // Creating a new account
                System.out.println("\t\t\t\t\t\t\t\tCreating a new account. Please enter a new username\n");
                String newUsername = scanner.next();
                System.out.println("\t\t\t\t\t\t\t\tPlease enter a password for the new account\n");
                String newPassword = scanner.next();

                usernames.add(newUsername);
                passwords.add(newPassword);

                System.out.println("\t\t\t\t\t\t\t\tNew account created. You can now log in.\n");
            } else {
                int index = usernames.indexOf(enteredUsername);

                if (index == -1) {
                    System.out.println("\t\t\t\t\t\t\t\tUsername does not exist\n");
                } else {
                    System.out.println("\t\t\t\t\t\t\t\tPlease enter your password\n");
                    String enteredPassword = scanner.next();

                    if (passwords.get(index).equals(enteredPassword)) {
                        System.out.println("\t\t\t\t\t\t\t\tWelcome user " + enteredUsername + "\n");
                        check = true;
                    } else {
                        System.out.println("\t\t\t\t\t\t\t\tUsername and Password do not match\n");
                    }
                }
            }
        }

        for (int i = 0; i < usernames.size(); i++) {
            System.out.println("Username: " +usernames.get(i) + "\tPassword: " + passwords.get(i));
        }
    }
}
