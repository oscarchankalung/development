# Send Multiple Attachments with FormData

## Model

```tsx
export interface IAttachment {
  type?: string; // e.g. 'audio/mp4' or 'image/jpeg'
  uri: string;   // e.g. '/Users/.../02AF85B9-533C-440B-B165-02E1C97813C3.jpg'
  name?: string; // e.g. '02AF85B9-533C-440B-B165-02E1C97813C3.jpg'
}

export interface ISendAttachmentMessageRequest {
  api_access_token: { name: 'api_access_token'; value: string };
  conversationId: { name: 'conversationId'; value: string };
  attachments: { name: 'attachment[]'; value: IAttachment };
}
```

## Example: Image

```tsx
const attachment = {
  name: '02AF85B9-533C-440B-B165-02E1C97813C3.jpg'
  type: 'image/jpeg',
  uri: '/Users/.../02AF85B9-533C-440B-B165-02E1C97813C3.jpg'
}
```

## Example: Audio

```tsx
const attachment = {
  name: 'sound.m4a'
  type: 'audio/mp4',
  uri: 'file:///Users/.../sound.m4a'
}
```

## API

```tsx
const sendAttachmentMessage = ({
  api_access_token,
  conversationId,
  attachment,
}: EConsult.ISendAttachmentMessageRequest) => {
  const path = SEND_ATTACHMENT_MESSAGE;
  const form = {
    api_access_token,
    conversationId,
    attachment,
  };
  const headerParams = {};
  return postForm({ path, form, headerParams });
};
```

## FormData

```tsx
export type Form = { [key in string]: string | any };

export const formToFormData = (form: Form) => {
  const formData = new FormData();

  Object.values(form).forEach(({ name, value }) => {
    const isValueArray = Array.isArray(value);

    if (isValueArray) {
      value.forEach(item => formData.append(name, item));
    }
    if (!isValueArray) {
      formData.append(name, value);
    }
  });

  return formData;
};
```

## PostForm

```tsx
const response = await fetchWithTimeout(
  path,
  {
    method: 'POST',
    headers: headerParams,
    body: formData,
  },
  timeout,
);
```

## FindFileType

```tsx
const findFileType: FindFileType = uri => {
  if (uri) {
    const extension = uri.split('.').pop() ?? '';
    const map: { [key in string]: 'image' | 'audio' } = {
      png: 'image',
      jpg: 'image',
      jpeg: 'image',
      mp3: 'audio',
      mp4: 'audio',
      m4a: 'audio',
      aac: 'audio',
      wav: 'audio',
      oga: 'audio',
    };
    return map[extension] ?? undefined;
  }
  return undefined;
};
```

## References

- [MDN - Web APIs - FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
- [Andy Kelso - Medium - sing FormData to Upload Multiple Images](https://kelsocode.medium.com/using-formdata-to-upload-multiple-images-73a6b1aaa179)