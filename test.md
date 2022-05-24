# Components

- [00 Common](#00-common)
- [01 WorksManagement](#01-worksmanagement)
- [02 WorksOrderDetails](#02-worksorderdetails)
- [03 ActionSummary](#03-actionsummary)
- [04 CMMSDetails](#04-cmmsdetails)
- [05 CMMSAttachment](#05-cmmsattachment)
- [06 UploadDetails](#06-uploaddetails)

## [01 WorksManagement](./01%20WorksManagement.md)

```tsx
// Common
<SearchBar/>

// WorksManagement
<WorksManagementGreeting/>
<WorksManagementFilter/>
<WorksManagementFilterButton/>
<WorksManagementItemList/>
<WorksManagementItemExcerpt/>
<WorksManagementItemText/>
```

## [02 WorksOrderDetails](./02%20WorksOrderDetails.md)

```tsx
// Common
<HeaderRightButton/>
<StatusBadge/>
<SearchBar/>

// WorksOrderDetails
<WorksDetailsHeader/>
<WorksDetailsOverview/>
<WorksDetailsOverviewText/>
<WorksDetailsRepairStatus/>
<CMMSRequestList/>
<CMMSRequestExcerpt/>

// ActionSummary
<ActionSummaryModal/>
```

## [03 ActionSummary](./03%20ActionSummary.md)

```tsx
// WorksOrderDetails
<WorksDetailsHeader/>

// ActionSummary
<ActionSummaryModal/>
<ActionSummaryHeader/>
<ActionSummaryList/>
<ActionSummaryExcerpt/>
```

## [04 CMMSDetails](./04%20CMMSDetails.md)

```tsx
// Common
<RoundButton/>

// WorksOrderDetails
<WorksDetailsHeader/>

// CMMSDetails
<CMMSDetailsOverview/>
<CMMSDetailsOverviewText/>
<CMMSDetailsAttachmentList/>
<CMMSDetailsAttachmentExcerpt/>

// AddAttachment
<AddAttachmentModal/>
<AddAttachmentButton/>
```

## [05 CMMSAttachment](./05%20CMMSAttachment.md)

```tsx

```

## 06 UploadDetails

<!-- ](./06%20UploadDetails.md) -->

```tsx
// Common
<HeaderRightButton/>
<RoundButton/>

// CMMSAttachment
<CMMSAttachmentCarousel/>
<CMMSAttachmentForm/>
```

## 00 Common

```tsx
<HeaderRightButton/>
<RoundButton/>

<StatusBadge/>
<SearchBar/>
```
