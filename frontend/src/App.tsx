import React from 'react';
import useWebSocket from 'react-use-websocket';
import * as Constants from './constants';
import {
    CurrentSessionTimeChart,
    FanDriveInputVoltageChart,
    WebsocketConnectionStatus,
    WebsocketMessage,
} from './components';
import { ReadResult } from './shared/types';

export const App = () => {
    const roomName = 'parameters';
    const url = `${Constants.WINDTUNNELS_WEBSOCKET_URL}/default/${roomName}`;

    const { lastJsonMessage, readyState } = useWebSocket(url);

    return (
        <div>
            <h1>
                Websocket connection status:{' '}
                <WebsocketConnectionStatus readyState={readyState} />
            </h1>
            <h2>Last message:</h2>
            <WebsocketMessage<ReadResult[]> message={lastJsonMessage} />
            <h2>Fan input voltage:</h2>
            <FanDriveInputVoltageChart readResult={lastJsonMessage} />
            <h2>Session time:</h2>
            <CurrentSessionTimeChart readResult={lastJsonMessage} />
        </div>
    );
};
