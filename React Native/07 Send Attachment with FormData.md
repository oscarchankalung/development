# Send Attachment with FormData

## Reference

[FormData - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/FormData)

## Model

```tsx
export interface ISendAttachmentMessageRequest {
  api_access_token: string;
  conversationId: string;
  attachment: {
    type?: string; // e.g. 'audio/mp4' or 'image/jpeg'
    uri: string;   // e.g. '.../02AF85B9-533C-440B-B165-02E1C97813C3.jpg'
    name?: string; // e.g. '02AF85B9-533C-440B-B165-02E1C97813C3.jpg'
  };
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

  Object.entries(form).forEach(([key, value]) => {
    formData.append(key, value);
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
