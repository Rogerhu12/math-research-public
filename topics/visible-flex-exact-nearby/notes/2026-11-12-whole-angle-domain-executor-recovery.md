# Whole-angle 域包的第二次执行器恢复登记

2026-11-12，constructive_route。

执行器再次更换后，未推送的第 419 段全角/复时间运行报告丢失。本次只从已完整保存于会话的文本恢复源码和数学证明，不以数值摘要拼造运行证书。

## 已逐字恢复并核对的文件

- scripts/fourfold_phase_full_angle_time_domain.py：
  SHA256 d681614326efacb0c256037d2c7e995eb895d8f77ce4281720f44c76a896548e，
  与丢失前完全相同；Git blob 348696ffbf2cf2f6577bd2e77eecb2ce3cf1330c。
- notes/2026-11-12-step5-whole-angle-complex-time-domain.md：
  SHA256 17aa802266c6e32deeba453d26c9e302fa754a90e89e74749d11569886401c5a，
  与已修正式 (7) form-feed 排版错误后的版本完全相同；Git blob
  ad884084ecb80f190b3a05f4ef03376f29216f4e。

数学证明可完整阅读；其中的历史完成数据必须与下面需要重新生成的报告配套。旧 manifest 不由摘要伪造。

## 必须实际重跑的报告

旧路径：
data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json

丢失前 SHA256 为
414a8cd3f1704c0abe7aee3b0b90a33c19e44ed425912898f4293c5a79487dcd，
328987 bytes。原运行完整处理三个 germ，约 105 秒，全部域门通过。
这些仅是重放对照，不能充当新执行器的证书。

报告包含运行时间字段，因此新运行的文件哈希可以不同；必须保存新实际输出并更新完成清单。新的有向数值与全覆盖通过状态要由程序重新生成，不手填。

## 准确输入与重放入口

目标参数为 δ5=−7789843107295549/4611686018427387904，
目标 object SHA256 91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848，
自身根证书 SHA256 489268d254c2a9454ccbee32a4821d9bf577279490f76c9cc6f8d902a5e64e0b。

时间网格来自已推送的 step4_shared1032_reference_forward/manifest.json，
SHA256 43cbffb2e0b924b6d69608df54e0acf3cf8ecd66c030b7343e84864ad6eb81a0。
准确端点为
4466727694628647/9007199254740992 与
282639970307159/562949953421312。
此域程序只读这个定义 manifest 的时间列表，不读 141 MB 的参考 shards，也不读旧 234 MB raw 轨迹。

从 topics/visible-flex-exact-nearby 执行：

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_phase_full_angle_time_domain.py --retarget data/phase_ring_continuation/step5_retargeted_reference/descriptor.json --segment 419 --time-radius 3 --larger-time-radius 4 --theta-strip 1/64 --wider-theta-strip 1/32 --time-order 40 --angles 1024 --cutoff 255 --primitive-nodes 512 --bits 192 --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json

两套 grid 依赖由 reproduce_newton 拥有；若未保存在 main，须从该代理的完整源码恢复，不能替换为仅有有限 primitive 的近似版本。独立完整数学/源码审查由该代理拥有，原审查 note SHA256
6f80a8891c3cb7cfddf0152824176a52164f7f63dd86aa37dacea036ddecbf1b。

## 尚未实现的下一接口

负 r 的 D 偶性、准确正弦径向位移界和 turn quotient 的整圆域适配在此次中断前只有数学推导，尚未写新源、没有运行证书。不存在可以移用的“已完成端点结果”。下一步需在独立新模块实现并直接运行；已冻结第 419 段源码保持不变。
