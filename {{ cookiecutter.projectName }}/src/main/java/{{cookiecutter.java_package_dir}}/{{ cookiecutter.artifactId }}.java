/**
 * JavaFX App Template:
 * creates a 640x480 window that shows
 * which versions of Java and JavaFX the app is using.
*/

package {{ cookiecutter.groupId }};

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;


/**
 * Application's Main Class.
*/
public class {{ cookiecutter.artifactId }} extends Application {

    /**
     * Creates the primary stage of the application.
     *
     * @param stage primary stage.
    */
    @Override
    public void start(Stage stage) {

        // get Java and JavaFX versions
        String javaVersion = System.getProperty("java.version");
        String javafxVersion = System.getProperty("javafx.version");

        // create a Label with the versions
        Label label = new Label("Hello, JavaFX " + javafxVersion + ", running on Java " + javaVersion + ".");

        // Place the label inside a scene
        Scene scene = new Scene(new StackPane(label), 640, 480);

        // Add the title to the scene.
        stage.setTitle("Hello World");

        // Add the scene inside the primary stage and make it visible on the screen.
        stage.setScene(scene);
        stage.show();
    }

    /**
     * Runs the application.
     *
     * @param args Command line arguments.
    */
    public static void main(String[] args) {
        launch();
    }
}
