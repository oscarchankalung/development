# Sample Component

```tsx
import React, { useEffect, useState } from 'react';
import { StyleSheet, View } from 'react-native';

// constants
import IMAGE from './constants';
import COLOR from './constants';

const CONSTANT = '';

interface Props = {...};

const Page = ({...}: Props) => {
  // constants
  const IMAGE = IMAGES.PAGE;
  const COLOR = COLOR.PAGE;

  // data
  const [state, setState] = useState<string>('');

  useEffect(() => {
    const response = call();
    setState(response);
  }, []);

  // onPress
  const onPress = () => console.log('onPress');

  return (
    <View/>
  )
}
const styles = Stylesheet.create({...})
```

## Identifiers

| Style            | Category                                                           |
| :--------------- | :----------------------------------------------------------------- |
| `UpperCamelCase` | class / interface / type / enum / decorator / type parameters      |
| `lowerCamelCase` | variable / parameter / function / method / property / module alias |
| `CONSTANT_CASE`  | global constant values, including enum values                      |
| `#ident`         | private identifiers are never used.                                |

* `IUpperCamelCaseParamsModel` : API Params Model
* `IUpperCamelCaseResponseMode` : API Response Model
* `UpperCamelCaseModel` : Component Model

## Others

* Avoid nesting and Write every statement in 1 line as much as possible
* Destructure a long statement by declaring variables if needed.