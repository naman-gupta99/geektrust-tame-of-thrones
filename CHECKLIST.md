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
