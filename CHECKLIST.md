# Checklist for the Project

## Logic Points

- [ ] Working Code
- [ ] Use factory patterns

```java
public interface PlayerStateAction {
  void execute(Player p);
}

public class DidNotBat implements PlayerStateAction {
  public void execute(Player p) {
    updateScoreCard()
    updateCommentary()
  }
}


public class PlayerStateActionFactory {
  public static PlayerStateAction getAction(String state) {
    switch (state) {
      case "DID_NOT_BAT"
        return new DidNotBat()
      //other states
      ...
    }
  }
}
```

- [ ] Rather than using Nested Loop, use a Straight Ladder
- [ ] Use a Flow of Code

## OOPS Points

- [ ] Classes
- [ ] Inheritence
- [ ] Private Variables
- [ ] PolyMorphism

## Testing Points

- [ ] Unit Tests vs Integration Test
- [ ] Name tests as so : `shouldRotateStrikeIfOneRunScoredAndIfOverNotFinished`
- [ ] The aim of a test should be singular

## Readability Points

- [ ] Small Functions (Break Large Functions into utilities or multiple functions)
- [ ] Use Classes and behaviours indtead of huge if else blocks
- [ ] Good and Meaningful Naming
- [ ] Constant Variables instead of Numbers
- [ ] Use Language conveentions
- [ ] Modularity is a must

## Data Structures Points

- [ ] Data needed to be binded toghether is better off binded structurally than logically (i.e. rather than array indexing make Classes)
- [ ] Use arrays only for sequential data, otherwise Maps

## Build Points

- [ ] Have a build file that installs all dependencies
- [ ] Have a way to run tests

## Extensibility Points

- [ ] No Duplication in the Code
- [ ] No Hardcoded Values
