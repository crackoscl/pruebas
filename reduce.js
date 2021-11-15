const receipts = [
  { id: 1, consolidated: false },
  { id: 2, consolidated: true },
  { id: 3, consolidated: false },
  { id: 4, consolidated: true },
  { id: 5, consolidated: false },
  { id: 6, consolidated: true },
];

const splitReceipts = (receipts) => {
  return receipts.reduce(
    (acc, receipt) => {
      const key = receipt.consolidated ? "consolidated" : "notconsolidated";
      return {
        ...acc,
        [key]: [...acc[key], receipt],
      };
    },
    { consolidated: [], notconsolidated: [] }
  );
};

console.log(splitReceipts(receipts));
