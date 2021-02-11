import React from 'react';

type Props<T> = {
    message: T;
};

export function WebsocketMessage<T>(props: Props<T>): React.ReactElement {
    const { message } = props;

    return <pre>{JSON.stringify(message, null, 4)}</pre>;
}
