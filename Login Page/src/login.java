import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;

public class login {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ArrayList<String> usernames = new ArrayList<>(); //Dynamic arrays
        ArrayList<String> passwords = new ArrayList<>();

        //Pulls data from txt file
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("C:\\Users\\shaza\\OneDrive\\Documents\\GitHub\\p33-budget-dashboard\\Login Page\\src\\userNamePasswordData.txt"))) {
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                String[] parts = line.split(", ");
                if (parts.length == 2) {
                    usernames.add(parts[0]); //Separates usernames and passwords and adds them to the appropriate arrays
                    passwords.add(parts[1]);
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading from the file: " + e.getMessage());
        }

        boolean check = true;

        while (check) {
            System.out.println("\t\t\t\t\t\t\t\tPlease enter your username or type 'new' to create a new account\n");
            String enteredUsername = scanner.nextLine();

            if (enteredUsername.equals("new")) {
                //Creating a new username and password
                System.out.println("\t\t\t\t\t\t\t\tCreating a new account. Please enter a new username\n");
                String newUsername = scanner.nextLine();
                if (usernames.contains(newUsername)) {
                    System.out.println("\t\t\t\t\t\t\t\tThat username is already taken\n");
                } else {
                    System.out.println("\t\t\t\t\t\t\t\tPlease enter a password for the new account\n");
                    String newPassword = scanner.nextLine();

                    //Adds new username and password to the dynamic array
                    usernames.add(newUsername);
                    passwords.add(newPassword);

                    //New username and password are added to the txt database
                    try (FileWriter fileWriter = new FileWriter("C:\\Users\\shaza\\OneDrive\\Documents\\GitHub\\p33-budget-dashboard\\Login Page\\src\\userNamePasswordData.txt", true)) {
                        fileWriter.write("\n" +newUsername + ", " + newPassword);
                    } catch (IOException e) {
                        System.err.println("Error writing to the file: " + e.getMessage());
                    }

                    System.out.println("\t\t\t\t\t\t\t\tNew account created. You can now log in.\n");
                }
            } else {
                int index = usernames.indexOf(enteredUsername);

                if (index == -1) {
                    System.out.println("\t\t\t\t\t\t\t\tUsername does not exist\n");
                } else {
                    System.out.println("\t\t\t\t\t\t\t\tPlease enter your password\n");
                    String enteredPassword = scanner.nextLine();

                    if (passwords.get(index).equals(enteredPassword)) {
                        System.out.println("\t\t\t\t\t\t\t\tWelcome user " + enteredUsername + "\n");
                        check = false;
                    } else {
                        System.out.println("\t\t\t\t\t\t\t\tUsername and Password do not match\n");
                    }
                }
            }
        }
    }
}
