-- schema.sql

CREATE TABLE talked_time_metrics (
                                     id SERIAL PRIMARY KEY,
                                     user_id UUID NOT NULL,
                                     session_id UUID NOT NULL,
                                     talked_time INTEGER NOT NULL,
                                     timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_talked_time_user_id ON talked_time_metrics(user_id);
CREATE INDEX idx_talked_time_session_id ON talked_time_metrics(session_id);
CREATE INDEX idx_talked_time_timestamp ON talked_time_metrics(timestamp);

CREATE TABLE microphone_used_metrics (
                                         id SERIAL PRIMARY KEY,
                                         user_id UUID NOT NULL,
                                         session_id UUID NOT NULL,
                                         microphone_used BOOLEAN NOT NULL,
                                         timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_microphone_used_user_id ON microphone_used_metrics(user_id);
CREATE INDEX idx_microphone_used_session_id ON microphone_used_metrics(session_id);
CREATE INDEX idx_microphone_used_timestamp ON microphone_used_metrics(timestamp);

CREATE TABLE speaker_used_metrics (
                                      id SERIAL PRIMARY KEY,
                                      user_id UUID NOT NULL,
                                      session_id UUID NOT NULL,
                                      speaker_used BOOLEAN NOT NULL,
                                      timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_speaker_used_user_id ON speaker_used_metrics(user_id);
CREATE INDEX idx_speaker_used_session_id ON speaker_used_metrics(session_id);
CREATE INDEX idx_speaker_used_timestamp ON speaker_used_metrics(timestamp);

CREATE TABLE voice_sentiment_metrics (
                                         id SERIAL PRIMARY KEY,
                                         user_id UUID NOT NULL,
                                         session_id UUID NOT NULL,
                                         sentiment_score REAL NOT NULL,
                                         timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_sentiment_user_id ON voice_sentiment_metrics(user_id);
CREATE INDEX idx_sentiment_session_id ON voice_sentiment_metrics(session_id);
CREATE INDEX idx_sentiment_timestamp ON voice_sentiment_metrics(timestamp);
