# R87 原 Python 线性校准：原盒内五点同号

2026-11-28，/root/design_continuation。**这是新的二维线性数值计算，不是 BVP 接受。**

执行环境恢复并由 root 完成公共/私库同步、核双 README 无差异后，本次真正执行冻结
`calibrate_single_gentle_profile.py`。它读取 R87 新六段 profile、真实原 M24 port、
原 chart、原 multistage provider 和原 ShortBridge，调用未改的 BackwardLine /
DOP853。没有采用另写的 JS ODE；V8 此前只做了精确标量证明及源字节 SHA 核对。

| δ | 原 core_z/core_R |
|---:|---:|
| .063 | .013534990209779208 |
| .06375 | .011465898940009187 |
| .0645 | .009424252367087022 |
| .06525 | .007409387459474281 |
| .066 | .005420661541295862 |

五点同号，程序按原设定真实退出 **2**，状态为
`new_profile_linear_root_not_bracketed_in_proved_box`。没有写出
`linear-root-profile.json`，没有宣布区间内无根、数学不存在或 BVP 失败。
这说明本次原 bracket 未定位根；不能将未校准 .0645 冒称新 profile 的已接受值。

实际调用从 15:26:02.788333 UTC 到 15:26:06.520080 UTC，父进程已 join。
用时 3.731583078 s，`RUSAGE_CHILDREN.ru_maxrss=80244 KiB`。首次 shell 调用因
`/usr/bin/time` 不存在返回127，发生在 Python 数学程序 spawn 之前；随后用
Python 父进程真实 wait/计时，没有重复五点计算。冻结源码 docstring 中“未运行”
描述的是发布时的准备状态，本条登记其第一次真实运行，不修改历史源码字节。

## 来源与输出

| 项目 | SHA-256 |
|---|---|
| 新校准源码 | af5bf8e544205e60eb39f32881639470495ff0ee26d7ff35ce3e476218bf3329 |
| 新 profile 初值文件 | e86bbebe8ae2c5842541772f8418c791b9ab622ab7ba25abcd9ec3feff2b2dff |
| 实际 M24 port | 42369d1571413fd4ecccea43ccfef233f4b97506f71e28b86ed9735c28c2d93b |
| 原 chart | dc85dda524e03896b4afa552bd1f859b73cf96f88033565ff910e227034f2f93 |
| 原 ShortBridge | 7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4 |
| 本次完整 calibration.json | 1f2ea915c659fdd944d1c2310e75081737504bb402c9bb6583f85d8afce21dec |
| 已 join 的 launcher 小记录 | 6e9c95e9e1ce197a7e064ebeae46c5bf002e71637c65fa0cbc41e789122b7714 |

实际工作根为
`/workspace/scratch/7c4e33ee17de/held10-design-work`。
完整返回在
`R87-single-gentle-linear-calibration-20261128/calibration.json`，
launcher 在 `R87-single-gentle-linear-launch-20261128.json`。
同名 observed JSON 记录完整实际 argv、所有直接源/input SHA 与这五个标量。

恢复后的真实 port 中 slope3 为 21.398688018893054，
backgroundSlope 为 .08000000000000027，backgroundSecond 为 −1.866666666666673；
没有将后两者替换为更简短的小数再声称原字节相同。它与 q012 物理 port 同 SHA。

后继先独立支付更宽 r 盒的连续首周期尺寸和较紧首片支撑，再仅补未算过的新 δ，
继承本五点的实际缓存。旧 R87 的原盒证明、原校准源码和返回均冻结，不机械放宽标签，
也不把这一线性输入校准当成完整非圆前缀或同 g 精化。
