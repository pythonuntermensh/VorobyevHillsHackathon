"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { useAppDispatch, useAppSelector } from "@/hooks/redux-hooks";
import { getFiles } from "@/http/files/filesAPI";
import { addDocuments, IFile } from "@/lib/features/files/filesSlice";
import { convertEnglishToRussian } from "@/utils/formateFileType";
import { createSelector } from "@reduxjs/toolkit";
import { ArrowLeft } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

const Page = () => {
  const [searchFileName, setSearchFileName] = useState("");
  const [searchFileType, setSearchFileType] = useState("");
  const [key, setKey] = useState(+new Date());
  const [value, setValue] = useState<string | undefined>(undefined);
  const dispatch = useAppDispatch();
  const router = useRouter();

  const selectFilteredFiles = createSelector(
    (state) => state.filesReducer.files,
    (files: IFile[]) =>
      files.filter((file) => {
        const fileNameMatch =
          file.name.toLowerCase().includes(searchFileName.toLowerCase()) ||
          file.keywords.toLowerCase().includes(searchFileName.toLowerCase());
        const fileTypeMatch =
          searchFileType === "" || file.class === searchFileType;
        return fileNameMatch && fileTypeMatch;
      })
  );

  let files = useAppSelector(selectFilteredFiles);

  useEffect(() => {
    getFiles().then((res) => {
      dispatch(addDocuments(res.data.files));
    });
  }, []);

  return (
    <div className="w-full h-full flex items-center justify-center p-2">
      <div className="bg-white p-3 rounded-lg w-[100%] md:w-[90%]">
        <ArrowLeft
          onClick={() => router.back()}
          className="w-8 h-8 rounded-full hover:bg-zinc-300 transition cursor-pointer"
        />
        <p className="text-xl font-semibold pl-0 p-4">Архив документов</p>
        <div className="flex flex-col md:flex-row md:gap-x-3 gap-y-3 items-center justify-center">
          <div className="md:flex-1 w-full">
            <Label htmlFor="document-name">Поиск по названию и ключевым словам документа</Label>
            <Input
              id="document-name"
              placeholder="Название документа/ключевые слова..."
              className="mt-1 focus-visible:ring-0 focus-visible:ring-offset-0"
              value={searchFileName}
              onChange={(e) => setSearchFileName(e.target.value)}
            />
          </div>
          <div className="md:flex-2 md:w-auto w-full">
            <Label htmlFor="document-name">Тип документа</Label>
            <Select
              onValueChange={(e) => setSearchFileType(e)}
              key={key}
              value={value}
            >
              <SelectTrigger className="w-[180px] mt-1">
                <SelectValue placeholder="Тип документа" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel className="w-full text-center">Выберите документ</SelectLabel>
                  <Button
                  className="w-full text-start px-2 bg-transparent hover:bg-white text-black"
                  size="sm"
                  onClick={(e) => {
                    e.stopPropagation();
                    setValue("");
                    setSearchFileType("");
                    setKey(+new Date());
                  }}
                >
                  ---
                </Button>
                  <SelectItem value="proxy">Доверенность</SelectItem>
                  <SelectItem value="contract">Договор</SelectItem>
                  <SelectItem value="act">Акт</SelectItem>
                  <SelectItem value="application">Заявление</SelectItem>
                  <SelectItem value="order">Приказ</SelectItem>
                  <SelectItem value="invoice">Счет</SelectItem>
                  <SelectItem value="bill">Приложение</SelectItem>
                  <SelectItem value="arrangement">Соглашение</SelectItem>
                  <SelectItem value="contract offer">Договор оферты</SelectItem>
                  <SelectItem value="statute">Устав</SelectItem>
                  <SelectItem value="determination">Решение</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </div>
        </div>

        <ScrollArea className="whitespace-nowrap w-full h-72 pr-2 px-3">
          {files?.map((file) => (
            <div
              key={file.timestamp}
              className="flex justify-between px-3 py-3 my-2 border-y-2 border-dashed border-zinc-400"
            >
              <Link
                href={`http://176.109.106.55:8000/files/download?class=${file.class}&name=${file.name}&timestamp=${file.timestamp}`}
                className="text-sky-500 font-semibold line-clamp-2 max-w-[80%] underline"
              >
                {file.name}
              </Link>
              <p className="text-zinc-600 font-bold">
                {convertEnglishToRussian(file.class)}
              </p>
            </div>
          ))}
          <ScrollBar orientation="horizontal" />
          <ScrollBar orientation="vertical" />
        </ScrollArea>
      </div>
    </div>
  );
};

export default Page;
