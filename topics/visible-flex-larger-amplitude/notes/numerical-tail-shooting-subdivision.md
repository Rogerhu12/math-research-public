# 同一实际尾的数值分片与条件数

## 实际发现

smallcut30、完整混合目标的低幅 \(\lambda=.25\) 在M24/N512、
physical depth8、shootingParts4/steps24下，将shooting残差从
\(6.68\times10^{-4}\) 降至 \(6.98\times10^{-8}\)，但没有达到原定
\(2\times10^{-9}\) 容差。此时几何状态与A最小值已不再发生可见变化，
源校正器的最大局部图矩阵条件数约 \(3.016\times10^8\)。该未收敛迭代
完整保留，并明确标记为interrupted、warm-only。

保持物理metric、完整H、M24/N512、物理depth8、floor=.05及原始每段
96个RK步不变，只将匹配节点改为shootingParts8/steps12后，矩阵条件数
降至 \(2.4533\times10^4\)。一次真实Newton校正将残差降至
\(2.36145\times10^{-10}\)，达到原容差。完整实际响应是
`numerical-m2-smallcut30-q02-tail24-parts8-solve-response_0001.json.gz`。

|实际有限尾量|结果|
|---|---:|
|首physical H|−6.658815252291785e−5|
|次physical H|−3.650497450402188e−6|
|shooting residual|2.36144819e−10|
|physical full Darboux|7.26552121e−15|
|actualMetric|8.66025199e−15|
|minA / minD|.661183733 / .999858473|
|formal κmax|7.994254694|

这是同一数值问题的条件数改善，未改变物理尾设计，也没有降低接受
容差。它不说明此前较强 \(\lambda=.5859375\) 的目标已经通过M24
精修；较强目标仍需从这个真正M24入口沿完整混合向量继续。

## 为什么原RK网格不变

令一个原始physical profile的参数为 \(t\in[0,1]\)。旧分片的RK
端点为

\[
t=\frac{p+k/24}{4}=\frac{24p+k}{96},
\]

新分片端点为

\[
t=\frac{p+k/12}{8}=\frac{12p+k}{96}.
\]

两者均为同一96步网格。RK4中点也相同；源cusp细分在相同的原始
physical参数位置插入断点。新增匹配节点是既有RK步的端点，故在
精确算术下，消去新增节点得到同一组有限RK流匹配方程。浮点重参数化
仍可能产生末位差异，不能声称整个计算逐位相同。

源 `950f-tail-subdivision.mjs` 同时将每个原raw cell的动量重标度
`portRatio=2**a` 只放在该cell唯一的外侧接点，其余新增接点的比值
均为1。因此细分没有重复加入或丢掉物理接口的归一化变换。有限尾
最深端的线性稳定图仍由同一个physicalDepth到同一个linearFar的原
cell传输产生；改变的是内部匹配图的因子分解和初猜，不是该远端条件。

源的校正器逐段求逆

\[
G_n=T_{11,n}+T_{12,n}G_{n+1}^{\rm stable},
\]

并报告 \(\|G_n\|_\infty\|G_n^{-1}\|_\infty\) 的最大值。
这是匹配图矩阵的条件数，不是动量root的正Gram矩阵条件数，也不直接
等于主曲率或reach。缩短局部传输区间改变了数值因子分解，因此可以
降低此条件数，而不改变上述离散边值问题。

## 真实warm转换，而非改标签

当前源 `78718-tail-geometric-warm-remesh.mjs` 只支持相同
shootingParts的角谱转换，不能直接读parts4状态作为parts8状态。
最初直接重启因这项明确兼容性检查退出，未执行数学求解。

新增 `computations/numerical-tail-subdivide-warm.mjs` 使用固定源
`950f-tail-warm-remesh.mjs` 的 `remeshCheckpoint`：

1. 严格核对所有物理参数、M、N、物理depth、容差和完整cut H；只允许
   数值分片、对应步数/审计步数、失败迭代上限和记录路径变化。
2. 原289节点全部原样复制，插入的中点由同一有限非线性RK场计算，
   得到577节点。检查原节点最大state改变严格为零。
3. 以新参数和正确节点数保存独立warm-only包，再让原source worker
   执行自己的几何一致性检查及原本的真实非线性求解。

转换记录是
`numerical-m2-smallcut30-q02-tail24-parts8-warm.json.gz`，包含所有数值
参数变化、旧checkpoint状态/哈希和逐项源哈希。它没有声称新增节点
已满足shooting条件。随后实际求解才给出上表的成功结果。

固定源revision为 `869436630c99aa5a68afb55bd8877c826034d117`。
原低幅未收敛状态与停止理由分别保存在
`numerical-m2-smallcut30-q02-tail24-low-iteration.json.gz` 和
`numerical-m2-smallcut30-q02-tail24-low-interrupted.json`。

## 跨分片比较归一化误差

源报告的 `normalizedFullDefect` 是

\[
\left|\mathcal D\,E^2r r_x/w^2\right|,
\]

其中 \(r_x\) 是当前subprofile参数的导数。parts4改parts8时，单纯
坐标缩放就会使这项数值减半。因此跨分片比较应优先使用physical
`fullD`、`actualMetric` 和曲率，或将源归一化缺陷乘以shootingParts，
恢复到原始physical profile参数。

上表实际M24解的源归一化缺陷为 \(8.40256548\times10^{-13}\)，恢复
到原profile参数后为 \(6.72205239\times10^{-12}\)。较强M16目标的
源值约.0098038954，对应原profile值约.0392155816；只有在同H下得到
M24真解后，才能比较这两档的精修效果。

## 有限预算后的严格同H比较

从 \(\lambda=.375\) 以较小步长继续，M24先后在
.40625、.4375、.46875、.5、.53125成功。.5625和.546875的切向
初猜在首次动量root评估被拒绝，缩步到.5390625后，真实Newton再次
收敛。原大步2次请求加这一路径8次请求用完预算；**没有达到原目标
.5859375**。不能把下面较低幅度的比较写成原目标已经精修成功。

随后对最后真点 \(\lambda=.5390625\) 作完整M24 audit，并从既有
M16 \(\lambda=.5\) 真包只追加一个相同H的M16解及audit。请求首项
为−1.43580703878e−4，第二项为−1.69726741810e−5；原16项逐值
完全相同，M24新增8项严格零。两档的全部非数值constructor字段和
19个共同源文件hash一致，每个原profile仍为96步。

|诊断|M16 / N256 / parts4|M24 / N512 / parts8|
|---|---:|---:|
|真实shooting残差|1.26851331e−10|2.19930043e−10|
|physical fullD|7.98793679e−6|2.65868838e−6|
|源normalizedFullDefect|.00185105093441|.000308049984311|
|原profile规范缺陷|.00740420373765|.00246439987449|
|actualMetric|8.93847218e−10|1.40945255e−10|
|formal κmax|8.02216693006|8.02216621207|
|minA|.222610258995|.222587068091|

物理Darboux缺陷和原profile规范量都下降到原来的.332837934倍，
约改善3倍。直接比较源normalized字段会得到约6倍，额外的2倍只是
分片坐标缩放，不能算成谱精度改善。改善后全尾二阶残差仍未达到
数值求解容差，metric较小也不能掩盖此事。

共同cut slope的最大变化为2.33e−11、second为5.42e−10，均值两项
的变化分别为9.32e−15和2.18e−12。端点D-N稳定并不推出全部内部
两jet已精修充分。M24的最坏Gauss缺陷在反射轴
\(r=.2770684831,\theta=0\)：形式主曲率一正一负，但其乘积误差
约为背景Gauss曲率绝对值的20%。最小A则在另一轴点，曲率只有
.004638；最大曲率8.022166在非轴点，那里Gauss缺陷约2.77e−13。

主报告是 `numerical-m2-smallcut30-q02-lambda05390625-refinement.json`，
位置报告是 `numerical-m2-smallcut30-q02-lambda05390625-curvature24.json`。
最终真实包分别为
`numerical-m2-smallcut30-q02-lambda05390625-tail16-response_0001.json.gz`
和 `numerical-m2-smallcut30-q02-tail24-parts8-finepath-response_0009.json.gz`。
严格比较入口可重放：

```bash
python computations/numerical-tail-compare-refinement.py \
  --coarse notes/numerical-m2-smallcut30-q02-lambda05390625-tail16-response_0001.json.gz \
  --fine notes/numerical-m2-smallcut30-q02-tail24-parts8-finepath-response_0009.json.gz \
  --out notes/numerical-same-height-refinement-replay.json
```

本记录仍是有限Fourier、有限径向、有限depth的数值证据。完整无限尾、
领口闭合、全相位全局reach和大幅held条件均未由本项结果证明。
