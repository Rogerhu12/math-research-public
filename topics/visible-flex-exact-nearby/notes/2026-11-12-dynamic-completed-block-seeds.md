# 只读动态完整 block 种子入口

新增三个控制层文件，不修改 frozen 数学 kernel：

- `fourfold_completed_block_seeds.py`：只读发现与字节身份闭包。
- `fourfold_forward_density_cover_v8.py`：在 root 原 v7 上接动态 g0 种子。
- `fourfold_parameter_density_cover_efficient_v4.py`：在原 v3 上接动态中心/整盒种子。

默认统一查找
`data/phase_ring_continuation/step5_ci_forward_blocks/*/block_*/block-manifest.json`。
显式静态 seed、既有完成前缀和已完成本地叶优先；只在需要新叶时发现动态 block。

## 必须通过的身份链

1. block 声明完整请求区间，descriptor 与完整真域 cover 的 SHA 相同；
   参数 scope 还要求中心及整盒 block 均完整。
2. 当前保存的 worker、g0/参数 pipeline、可选 precompute 源均匹配记录 SHA。
3. `files.json` 精确指向同一 block-manifest SHA，逐文件核 size 与 SHA；
   所有报告都在该清单内，完整有限矩形及原 first 数据没有被跳过。
4. 候选叶精确 `(segment,left,right)` 一致，实际 domain 在请求清单内且 SHA 相同。
   实际 g0 和两参数报告的 source/dependency SHA、完整标记、reference identity 全部核对。
5. 参数候选额外要求其 `g0_report_sha256` 与当前覆盖器已经选择的 g0 报告 SHA
   **逐字相同**；仅是同一曲面或同一时间段不够。

发现器返回候选后，controller 先保存该 manifest 和 inventory 的 SHA 证据，
随后仍调用原来的 `validate_saved` 或 `validate_parameter_report`。
g0 的完整 first integral 仍由原验证器解码、核同 identity/系数 SHA 并进入完整有序累计。
没有把 block 内局部积分直接当全局有序积分；跨块项由连续覆盖器照原公式保留。

正在下载且尚无最终 `files.json` 的目录不算本地完成种子。
已出现的完整身份冲突、字节变更、缺失 inventory 文件会失败退出，不能弱化验证后接受。
所有发现均只读，既不改 block 的 manifest，也不改其报告或有限系数。

## 实际验证范围

使用现有真实 `local_actual55/block_0055_0056` 完整块，分别发现 g0、center、uniform。
g0 经原 `validate_saved`（完整 first integral）通过；中心及 `+/-1e-9` 整盒经原
`validate_parameter_report` 通过。以不相同的 selected-g0 SHA 调用时没有返回参数候选。
记录在 `notes/2026-11-12-dynamic-block55-seed-validation.json`，SHA256
`06f4981a093fb842fc3514db3c6d4de17ac771a600ba08513217201f31b49d8e`。

此次只读核验没有重采样第 55 段，也没有声称远端 CI 已完成。
实际完整前腿仍需所有 550 段及最终精确 chronological merge；R31、非线性/PDE
与题目完成标准没有因本控制层改动而自动成立。
