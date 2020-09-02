import React from 'react'
import { InputProps } from './../constants/Interfaces'
import styles from './../css/components/input.module.css'

export function Input(props: InputProps){
    return (
        <input
            type={props.type}
            className={styles.input}
            placeholder={props.placeHolder}
        />
    )
}