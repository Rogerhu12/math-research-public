# 原 M12 尾端点的定点恢复与准确有理积分

2026-11-26，Astra-visible-flex-6a65e705/g5_and_exact。

为使全位置求解器真正消费原 common-cut v2 的完整定义，本次恢复并消费了原尾的全部
24 个历史 gzip blob，总计 80,730,280 bytes、18,552 个径向 span、141 个系数。
每次只在内存保留一个数据块，未把这些可再生 payload 写回仓库或 scratch。
最终以 Fraction 算出准确积分端点，缓存仅 23,133 bytes。
这是既有尾定义的重新消费，不是新的尾解，也不是新的数学存在结论。

## 1. 定义与核验

原 manifest 是 `2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json`，
SHA256 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。
历史 public commit 为 `aed993f7bd33fc6f545f941171c1b78d67258cca`，
其本课题 notes tree 为 `b15d0eaf9ab23bb70f4fb7a0a77dd3d9c1af45ad`。
24 个 blob SHA 固定写在新恢复脚本中，从该 tree 逐一核得。

每块都检查 Git blob SHA1（包括 `blob <length>\0` 头）、原 manifest SHA256、
原压缩字节数、数组形状，以及相邻块共有端行逐字相等。
径向长度为 $L_i=\alpha\ell_i$，其中 $\ell_i$ 是原准确 binary64 数，
$\alpha$ 是 manifest 的准确有理 normalization。程序还准确检查
$r_{\rm inner}+\alpha\sum\ell_i=r_{\rm cut}$。

对每个 Cartesian Fourier 系数，原 integrated-Fr 定义为

$$
V_{\rm end}=V_0+
\sum_i L_i\left[\frac7{30}(F_{r,i}+F_{r,i+1})+
\frac8{15}F_{r,i+1/2}+\frac{L_i}{60}(F_{rr,i}-F_{rr,i+1})\right].
$$

新脚本只把同一有限和整理为

$$
S_1=\sum_i\ell_i[7(F_{r,i}+F_{r,i+1})+16F_{r,i+1/2}],\quad
S_2=\sum_i\ell_i^2(F_{rr,i}-F_{rr,i+1}),
$$

$$
V_{\rm end}=V_0+\alpha S_1/30+\alpha^2S_2/60.
$$

所有输入 double 先用 `Fraction.from_float` 转准确分数，全部累加和乘法均用 Fraction。
缓存同时给分子、分母及数值显示；后者不取代准确有限和。
外端一、二阶径向系数仍是最后源行的准确 binary64 数。
没有用尾的存储位置列替代 integrated-Fr 的真实端点。

## 2. 真实运行与重生

源码 `../scripts/6a65-m12-stream-tail-exact-endpoint.py` 的 SHA256 为
`eac76884c7d7853e871eb5bd95f2bcc6a7bbce9c1f4299a1c0bfd0291f57c865`。
从仓库根执行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-stream-tail-exact-endpoint.py \
  --manifest topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-tail-exact-endpoint.json
```

实际 exit 0，176.183603374011 秒。
当共享 IP 的 GitHub 匿名 API 限流时，脚本可从进程环境变量 `M12_RECOVERY_TOKEN` 读取已授权凭据；
凭据不写文件、不写报告、不打印。所有网络请求仅按已知 blob SHA 读取公开源对象。
报告 SHA256 为 `38d7ab7d4155b2d945d2f8142c9f1b4a55eddd040b6431a93df834b5b1ecfa4f`，
端点缓存 SHA256 为 `a238ac45ce5b881c8b7e2d9c5db90e4bab30525bf40f6b445ef62e21d75539b8`。
重跑时须使用新输出路径；报告含运行秒数。

曾尝试只读 fetch 已知旧 head，但服务器返回包时遇到 tmpfs 空间不足而 exit 128。
该次未 checkout/pull/rebase；自然退出后只删除了该次未注册的 `tmp_pack_LFVfSK`（1,306,624 bytes），
没有删除注册 pack 或任何工作源。之后通过 GitHub commit/tree 元数据找到已知 blob，
改用上述定点流式消费，避免再拉整库历史对象。

## 3. 后续消费范围

准确端点足够重建 `db6f-root-common-cut-v2.py` 的原 267-span C2 correction，
包括准确 bridge 比例 $\lambda$ 和同一 height gauge。
该 $r=.6$ 截线是前缀与非圆尾的**内部接缝**，不是最终平截口。
统一求解器若暂时保留它的两 jet，只能报告完整前缀的有限改善；
真正全域还须让这条内部接口与尾一起联动，并到真实平领闭合。
