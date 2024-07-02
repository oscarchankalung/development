# Sample React Component

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

## Rules

* Write code in order

```
> import
> constants
> interface
> component
  > styles / constants
  > useState / useEffect / onPress() / render()
  > return
> stylesheet
```

* Write import statements in category and order if many

```
> react / react-native / dependenies
> constants
> components
> functions / apis / utils
```
