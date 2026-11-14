# 宏观 M12 最终联解的同度量端点闭合账本

状态：**保存的有限端点 Fourier 多项式有严格有理误差界；它们与真实源解的关系仍是数值证据。** 不宣称无限非线性尾存在。

输入为最终 prefix+tail 真联解
`notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64_tail_0018.json.gz`。冻结的几何、有限 calibration 系数和度量没有改变；改变 $N$ 只是取同一 CP 的不同深度端迹，随后在同一旋转背景上使用 R6 多项式圆领。

生成命令，在本题目录运行：

```sh
node scripts/db6f-tail-collar-packet.mjs \
  notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64_tail_0018.json.gz \
  notes/2026-11-09-db6f-tail-collar-flat17-m12-depth6-12-q512.json \
  --source-root repro/source-root --nodes 6,8,10,12 --angular-nodes 512
```

之后运行已经独审的有理算术验证器：

```sh
python scripts/db6f-audit-tail-background-and-packet.py \
  notes/2026-11-09-db6f-tail-collar-flat17-m12-depth6-12-q512.json \
  notes/2026-11-09-db6f-tail-collar-flat17-m12-depth6-12-exact.json
```

| 深度 $N$ | $K_N$ 上界 | R6 metric 上界 | 完整张量上界 |
|---:|---:|---:|---:|
| 6 | $3.10908\times10^{-10}$ | $2.08649\times10^{-11}$ | $4.27310\times10^{-8}$ |
| 8 | $1.32972\times10^{-21}$ | $1.51758\times10^{-23}$ | $1.80088\times10^{-19}$ |
| 10 | $3.29791\times10^{-33}$ | $7.54136\times10^{-36}$ | $4.45564\times10^{-31}$ |
| 12 | $5.64626\times10^{-45}$ | $2.72719\times10^{-48}$ | $7.62470\times10^{-43}$ |

表内显示值向上取整；精确 Fraction 结果在 JSON 内。$K_N$ 是已审 R6 端迹加权范数，不是曲率本身。此处采用背景曲率粗界 $6.001$，它覆盖已审全背景的 $6$ 上界。

数据包 SHA256 为 `ed0acd7e61c21909882456fbd4ed2dc922e575609e9f618feefc0d1e2445ec3c`，255,217 字节；有理账本 SHA256 为 `c1b0807bcd79a0afc04a19ea8b8bb9cb51bc22c711d6af43d02b71505e6fb2fa`。生成脚本与输入 SHA 均嵌入包内。

## 不可省略的范围限制

1. 每个端口的非径向平均高度都独立取零。若要比较完整外域图，须另控这些高度规范之间的差，不能直接把表当成完整 $C^2$ Cauchy 界。
2. 包里的端迹是有限角 Fourier 多项式及二进系数的精确定义。径向平面二阶源数据使用已记录的有限差分，未给源真导数的严格误差界。
3. 此包的角投影保留到 256 阶，完整 M12 XYZ 导出采用平面 signed modes 到 192 阶、精确保存高度的 12 个模。二者是略有差异的有限端迹，不能声称是同一份完整图证书。
4. 当前完整 M12 uniform 图自己的圆领已由 `db6f-tail-first-bounds.py` 直接验证，一阶全尾报告为 `notes/2026-11-09-db6f-tail-first-flat17-m12-uniform.json`；其中实际圆领的高度 $rr$ 上界为 $1.04952\times10^{-21}$。这一报告针对自己的保存系数，不挪用上表的端迹。
5. 同一个有限 CP 的多个端口不会证明无限非线性尾存在。上表支付的是同一度量上有限闭合操作的深度误差预算，并表明宏观候选的闭合项远低于当前求解容差。
