export interface Route {
    name: string
    path: string
    component: any
}

// State
export interface Product {
    id?: any
    name: string,
    price: string,
    validity: boolean | string,
    category: "carboidratos"
    | "verduras e legumes"
    | "frutas"
    | "leite e derivados"
    | "carnes e ovos"
    | "leguminosas e oleaginosas"
    | "oleos e gorduras"
}

// Components
export interface InputProps {
    type: "text" | "password"
    placeHolder: string
}

export interface TableProps {
    columns: Array<string>
    data: Array<Product>
    rowDataSelected?: any
    action?: any
}