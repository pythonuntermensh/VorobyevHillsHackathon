import StoreProvider from '@/components/providers/redux-store-provider'
import './globals.css'
import type { Metadata } from 'next'
import { Open_Sans } from 'next/font/google'

const font = Open_Sans({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Vorobyev hills',
  description: 'Try our application for documents classification',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ru">
      <body className={font.className}>
        <StoreProvider>{children}</StoreProvider>
      </body>
    </html>
  )
}
