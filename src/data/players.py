from lib.models.data.data import Data, IntData, PositionData, PostureData, StringData, UIDData, BBoxData

player_stats = Data(data={
    "points": IntData(value=0),
    "passes": IntData(value=0),
    "rebounds": IntData(value=0),
    "interceptions": IntData(value=0),
    "blocks": IntData(value=0)
})

pose_data = Data(data={
    "position": PositionData(),
    "posture": PostureData(),
    "bbox": BBoxData()
})

player_data = Data(data={
    "name": StringData(),
    "posture": pose_data,
    "player_stats": player_stats
})