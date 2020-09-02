import React, { useState, useEffect } from 'react'
import Header from '../components/Header'
import { Product } from '../constants/Interfaces'
import { requestApi } from '../constants/Functions'
import Table from '../components/Table'

export default function Home(){

  const [products, setProducts] = useState<Product[]>([])
  const columnsTable = [

  ]

  const request = async () => {
    const data = await requestApi("GET", "produto")
    setProducts(data)
  }

  useEffect(() => {
    request()
  },[])

  return (
    <div>
      <Header />
      <div>
        <Table 
          columns={["Nome", "Preço", "Validade", "Categoria"]}
          data={[{
            name: "Osvaldo",
            category: "carboidratos",
            price: "123",
            validity: String(true)
          },
          {
            name: "Osvaldo",
            category: "carboidratos",
            price: "123",
            validity: String(true)
          },
          {
            name: "Osvaldo",
            category: "carboidratos",
            price: "123",
            validity: String(true)
          }]}
        />
      </div>
    </div>
  )
}