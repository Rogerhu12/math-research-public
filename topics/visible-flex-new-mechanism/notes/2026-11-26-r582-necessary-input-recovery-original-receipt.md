# R582 必要续态输入恢复的原终态收据

2026-11-26；此为失联后的必要数据恢复，没有重新计算任何数学候选。

## 原始身份与真实结果

恢复 run **45839756631**、job **139977999607**，source **67771b35a44860689e39e4175f2b65220c55407c**；workflow `.github/workflows/visible-r582-recover-finite-input-20261126.yml`。自然终态 success；run 于14:30:47UTC创建、14:31:11UTC结束。完整原stdout仅在自然终态后读取一次，UTF-8（含BOM）349351 bytes，SHA256：

`797933116e0c3be196a86a35986259c48af370e5e04b511b031e1a620f0bc9c7`。

同一正式入口仅做stdlib HTTP/JSON/hash恢复。其实际wall为4.237356066000018秒；新科学模型求值、旧优化重放均为0。原日志和大FIELD数组不保存到Git或artifact。

## 被恢复的旧科学来源

正式恢复器读取已自然终止的run45827253372/job139934478969（source d4a5b41506139a2bd7ad6d53a473e1766f536377），并严格命中：

- 原raw12912168 bytes，SHA256 `0f8c0ea00bf770412d0b532dc8d28dd1d7ff0c8c2c51a874e11023e9a2432feb`；
- 原FINAL JSON447283 bytes，SHA256 `397a1a6fb7999c36f4849956ef6b820ba615118ce9733ebf0e6356a6ecbfb169`；
- 失联前尚未发布的必要配置218542 bytes，SHA256 `470a67d1b19249bdd08fc8b63cd129c12a4bf71b8e30c5b24a51c0ef496d0e3b`。

只补已发表原收据commit/path/hash后，新的实际source-state字符串为218828 bytes，SHA256：

`2e8a7c17398dde5e2e9fedfdf39f81823664b3861e3a33b6563da633b8fd5b91`。

其stdout NEXT_INPUT JSON220649 bytes，SHA256 `c8726e4bd730df833c5aa1cee1470ec5a6e87d28303273144126ce0950c45838`。配置只含下次必要实际q、材料位置和已有成本，不含dense端点大数组。

恢复后的纯stdlib核验再次给出：实际保留81q binary64 SHA d4afde612de65692d4f0184948565ca13b39a4bc04d85429a9103fae7e41f2b0；原124个实际圈SHA ba94cc842802e847e2d65a73a0a2eda0d29fe50a81ae77dfca99a4ddf512f059；4811基础点、5911材料位置、实际圈及相邻中点准确并集10835个位置，SHA5205d5a834717e06250bcbb1f98bec1139130ed42c20ed7e77d274ccf6346f52。剥去本次续态与成本后，原98910B input SHA187a463fdd777d2884310ac0793ed96583d5216d47407795b53daae633c46ac4准确恢复。未接受的backend末trial不作为新输入。

## 实际pull与范围

public actual pull 14:31:04.390491–04.756093UTC，从67771b35…至8bed9c0efe6bdca745b65dba7eb8f8d702c3ed5e；根与课题README blob均未变，差异空。private actual pull 14:31:06.809509–07.346344UTC，前后均cbdb77bda461f510b4685e9be7b31253ddd8bbec；根README blob未变，QUEUE仍为本会话进行中，未公开私有正文。

该恢复不改变原有限候选的失败判定，也不支付新97维算子的科学费用。它提供精确下一输入，使同p=.181的新实际尾形自由列可以继续；完整有限非圆、固定g精化、连续reach和主课题完成均未宣称。

## 开发记录

恢复后，子agent曾把228992B的下一请求经create_blob写成未挂接blob8bf312258cdf75ae8e4479d750a2c20fd7eb17bd，超过根规矩8的集成100KB限制。这是本轮第四次已披露开发偏离；已停止此传法。该输入仅含后续实际所需状态，本次正式发布使用本地认证git，不保存原raw，不切块，也不以超限checkpoint代替合规发布。
