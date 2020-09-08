import React from 'react'
import styles from './../css/components/modal.module.css'

export const Modal = (props: any) => {
    return (
        <div className={styles.container}>
            {props.children}
        </div>
    )
}