/**
 * Test template.
 *
 * This file will import and test code from the src/main/java folder.
*/

package {{ cookiecutter.groupId }};

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;

/**
 * Executes simple test cases.
*/
class TestApp {

    @Test
    void testExample1() {
        assertTrue(123 == 123, "123 should be equal to 123");
    }

    @Test
    void testExample2() {
        assertFalse("prova" == "test", "\"prova\" should NOT be equal to \"test\"");
    }
}
