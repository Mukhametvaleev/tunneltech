import React, { ReactElement } from 'react';
import { ReadyState } from 'react-use-websocket';

type Props = {
    readyState: ReadyState;
};

export const WebsocketConnectionStatus = (props: Props): ReactElement => {
    const { readyState } = props;

    const connectionStatus = {
        [ReadyState.CONNECTING]: 'Connecting',
        [ReadyState.OPEN]: 'Open',
        [ReadyState.CLOSING]: 'Closing',
        [ReadyState.CLOSED]: 'Closed',
        [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
    }[readyState];

    return <>{connectionStatus}</>;
};
