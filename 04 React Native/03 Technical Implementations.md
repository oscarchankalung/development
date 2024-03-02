# Technical Implementations

## Interface

- How to handle container style in react native?
  1. Wrap component with view container at screen
  2. Pass containStyle as prop from screen into component
  3. Define containerStyle on component
<!--  -->
- How to handle spacing between excerpt?
  1. Define `ItemSeparatorComponent` in `FlatList`
  2. Define `marginHorizontal` in excerpt
  3. Provide separator manually
<!--  -->
- How to handle touch events in subviews?
  1. Define `pointerEvents` in `View`
  2. Wrap subview in `TouchableWithoutFeedback`
<!--  -->
- How to handle onPressBackdrop in Modal?
  1. Define `onPressBackdrop` in `react-native-modal`
  2. Wrap subview in `TouchableWithoutFeedback`
<!--  -->

## Data Flow

- How to interact with header in screen component?
  1. Use `navigation.setOptions` >= 5.x ([reference](https://reactnavigation.org/docs/5.x/header-buttons#header-interaction-with-its-screen-component))
  2. Use `navigation.setParams` and `navigation.getParams` <= 4.x ([reference](https://reactnavigation.org/docs/4.x/header-buttons#header-interaction-with-its-screen-component))
<!--  -->
- How to handle empty list in FlatList?
  1. Define `ListEmptyComponent` in `FlatList`
  2. Use condifitional rendering

## API Call

<!--  -->
- How to handle loading state in react native?
  1. On http client's interceptor
  2. On indivdual API call
  3. On indivdual component