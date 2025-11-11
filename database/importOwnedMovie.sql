CREATE OR ALTER PROCEDURE [dbo].[importOwnedMovie]
AS
BEGIN TRANSACTION
    SET XACT_ABORT ON
    SET NOCOUNT ON

    INSERT INTO [dbo].[owned_movie](user_id, movie_id)
    SELECT distinct T.user_id, TD.movie_id
    FROM [dbo].[transaction_detail] TD
    JOIN [dbo].[transaction] T ON T.id = TD.transaction_id
    WHERE T.status = 'completed';

COMMIT TRANSACTION
GO

EXECUTE [dbo].[importOwnedMovie];