# 冻结有限头校准的实际几何核验

**实现核验；不产生新的非线性尾解或曲面。**

`strong_frozen_calibration_factory.mjs` 的唯一数值替换是：原
`physicalCell` 在 n<160 时读取已有 ledger 的二进制 alpha。
每次读取守卫 n、delta、R、c、lengthScale、A、calibrationSteps；
原 160 层、全局 warp alpha、原 far170 辅助图以及全部物理积分顺序
保持原定义，n>=160 仍执行原校准。未保存的六个校准诊断字段使用
throw getter，绝不伪造。此入口不把 rational65/64 深尾引入旧 stored g。

恢复后的实际 geometry-only 运行 session 51788 已 poll exit 0，
wait4 为 exit 0，wall 4.420698 秒、user 3.710737 秒、峰 RSS 92352 KiB，
Node heap128。工厂 SHA 为
`77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247`；
检查脚本 SHA 为
`711bd993db037c5b4f58020b31b021c89a93a8ded9bcee0595aeb7ccb5cc1780`。

完整报告 `2026-11-12-strong-frozen-calibration-recovered-geometry-r1.json`
实际确认：

- rational ready 旧 160 层头的五点 fingerprint 逐位一致：
  `645aec8c73e8da019657c0e4ad7c76ea0ac02f635e1bef415e0d33d49d19f6a2`。
- stored ready 的七点 fingerprint 逐位一致：
  `8a87255bf9e025190a1a98ff800859f05f95a94113045a60af9391fcace51d24`。
- 全局 alpha 仍为 `161.27721826272244`，实际原辅助 far 图仍构造。
- 六个不可提供的校准诊断字段访问都按预期拒绝。

本次 `compareOriginal=false`：比较的是已归档的原 ready 指纹，
没有再现场重算原 160 次校准，也未宣称所有连续点逐位相同。
同 g 的实现理由来自唯一替换点、全量二进制参数守卫和未改的物理
装配公式，实际指纹比较是其可复核数值检查。它不代替源积分误差证明。

最短接口：

```js
const reuse = await createFrozenCalibrationFactory(config, {
  sourceTopic,
  ledgerReadyFile,
  storedReadyFiles: [storedReadyFile]
});
const factory = reuse.factory;
const physical = factory.assemble();
```

返回对象另含 `manifest, reference, verify, physicalModeColumn,
idealModeGraph`。`assemble()` 自动执行已配置的指纹守卫。
固定 ledger/config 的哈希及完整命令在
`2026-11-12-strong-frozen-calibration-recovered-plan.json`。
核验后数值槽已正式交给 root 的真实 M20 完整 H 尾审计；本报告本身
没有执行 DN、Newton 或稳定图非线性求解。
