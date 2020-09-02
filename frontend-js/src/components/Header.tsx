import React from 'react'
import styles from './../css/components/header.module.css'
import { Input } from './Input'

export default function Header(){
    return (
        <div className={styles.header}>
            <Input 
                type={"text"}
                placeHolder={"Digite o produto desejado..."}
            />
        </div>
    )
}