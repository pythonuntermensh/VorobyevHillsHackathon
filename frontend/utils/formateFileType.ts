const englishToRussian: Record<string, string> = {
  proxy: 'Доверенность',
  contract: 'Договор',
  act: 'Акт',
  application: 'Заявление',
  order: 'Приказ',
  invoice: 'Счет',
  bill: 'Приложение',
  arrangement: 'Соглашение',
  'contract offer': 'Договор оферты',
  statute: 'Устав',
  determination: 'Решение',
};

export function convertEnglishToRussian(englishName: string) {
  return englishToRussian[englishName] || englishName;
}