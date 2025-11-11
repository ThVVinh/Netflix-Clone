CREATE OR ALTER PROCEDURE [dbo].[GenerateTransaction]
    @rows INT = 10000
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRANSACTION;
        WHILE @rows > 0
        BEGIN
            DECLARE @TransactionId INT;
            DECLARE @TransactionDate DATETIME;
            DECLARE @UserId INT;

            SET @TransactionDate = DATEADD(
            DAY,
            ABS(CHECKSUM(NEWID())) % DATEDIFF(DAY, '2024-01-01', '2025-12-31'),
            '2024-01-01'
            );

            SET @UserId = (SELECT TOP 1 id
            FROM [dbo].[user]
            ORDER BY NEWID());

            INSERT INTO [dbo].[transaction] (user_id, transaction_date, status)
            VALUES (@UserId, @TransactionDate, 'Completed');

            SET @TransactionId = SCOPE_IDENTITY();

            DECLARE @rowsInserted INT = FLOOR(RAND() * 6) + 1;

            ;WITH RandomMovies AS (
                SELECT TOP (@rowsInserted) id
                FROM [dbo].[movie]
                ORDER BY NEWID()
            )
            INSERT INTO [dbo].[transaction_detail] (transaction_id, movie_id, price)
            SELECT @TransactionId, id, 1.0
            FROM RandomMovies;
            SET @rows = @rows - 1;
        END
    COMMIT TRANSACTION;
END;
GO

execute [dbo].[GenerateTransaction];

-- DELETE FROM [transaction]
-- DBCC CHECKIDENT ('dbo.transaction', RESEED, 0);