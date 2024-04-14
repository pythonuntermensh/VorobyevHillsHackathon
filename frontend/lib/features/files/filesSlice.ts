import { createSlice, PayloadAction } from "@reduxjs/toolkit";

type FileType =
  | "proxy"
  | "contract"
  | "act"
  | "application"
  | "order"
  | "invoice"
  | "bill"
  | "arrangement"
  | "contract offer"
  | "statute"
  | "determination";

export interface IFile {
  class: FileType;
  name: string;
  timestamp: string;
  keywords: string
}

interface IFilesState {
  files: IFile[];
}

const initialState: IFilesState = {
  files: [
    // { name: "name1", class: "proxy", timestamp: "1233" },
    // { name: "name2", class: "contract", timestamp: "1234" },
    // { name: "name3", class: "act", timestamp: "1235" },
    // { name: "name4", class: "application", timestamp: "1263" },
    // { name: "name5", class: "order", timestamp: "1237" },
  ],
};

export const filesSlice = createSlice({
  name: "files",
  initialState: initialState,
  reducers: {
    addDocuments: (state, action: PayloadAction<IFile[]>) => {
      state.files = action.payload;
    },
  },
});

export default filesSlice.reducer;

export const { addDocuments } = filesSlice.actions;
