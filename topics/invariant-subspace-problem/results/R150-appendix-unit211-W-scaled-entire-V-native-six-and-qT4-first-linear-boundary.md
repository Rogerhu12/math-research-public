# 全余 W 的完整 Vlow 原六列返回与 qT4 二列：实际完成范围和冻结边界

日期：2026-11-28（Asia/Taipei）。Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**状态：三个缩放原值及完整 Vlow 六列已返回；qT4 的首次 alpha、chi 二列已返回。随后 Vlow 的换基阶段达到180秒边界，未形成它的二列或任何新 pair。** 不声称完整二值二列门成功，不重启该尾段或提高预算。

## 1. 完整原值的已成身份

沿[全原 alpha、chi 图](../results/R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md)及[低 D 次原值压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)的当前 W、D 非零范围。ell、m=u-ell、M 和原 native 纯权分母已付，不把该原图的排除移到一般 h=k。

记
$$
D=\ell(2\lambda^2-2\lambda+1)-T^2,\qquad
K_{\rm val}=\ell^2(4\lambda^3-6\lambda^2+3\lambda-1)
-3\ell(2\lambda^2-2\lambda+1)T+2T^3.
$$
用同一个完整原 N4 取
$$
\widetilde V_0=(\ell,\ell(\lambda-1-T),\ell+T,\ell+T),
$$
$$
\widetilde V_1=(0,0,m-\ell\rho,m+\ell\rho),\qquad \rho^2=1-Q,
$$
以及完整的常数、极化和二次项
$$
\widetilde Z_0=N_4(\widetilde V_0),\quad
\widetilde Z_2=N_4(\widetilde V_1),\quad
\widetilde Z_1=N_4(\widetilde V_0+\widetilde V_1)-\widetilde Z_0-\widetilde Z_2.
$$
它们的 rho 奇部实际为零。三个输入逐一在未改动的旧 C9 reducer 中完成原迹和旧分母范围断言；不是删除或放宽17703失败处的断言。

由 N4 的齐次二次性，完整原条件为
$$
V_{\rm low}=\ell^{-2}
\left(D\widetilde Z_0+\frac{K_{\rm val}}{2m}\widetilde Z_1+
\frac{D^2}{M}\widetilde Z_2\right).
\tag{1}
$$
ell 的逆只用于最后纯权六行，六个缩放乘积全部实际核回。因此 (1) 是整个 N4(V) 的原来源，不是某个分量或 Phi 倍数。

## 2. 真正 native 六列与来源

令
$$
b=(1,x,y,t,y^2,yt)^{\mathsf T},\qquad
F=(E_1,E_{B,e},E_{B,o},N_1,NS,PS).
$$
本次必要构造中的十二个 lambda、T 动作逐列返回
$$
M_\theta b-\theta b=E_\theta F.
$$
每个原误差的 NS、PS 坐标为零。后继节点满足
$$
r_{\theta v}=r_vM_\theta,\qquad
r_{\theta v}b-\theta P_v=(r_vE_\theta+\theta\tau_v)F
$$
只要 $r_vb-P_v=\tau_vF$。完整来源按实际父节点、原误差和纯权系数保留，不假六个原生成元自由或动作矩阵在自由模上交换。

本次确已形成
$$
r_Vb-V_{\rm low}\in(E_1,E_{B,e},E_{B,o},N_1)
\tag{2}
$$
的完整可再生来源及实际六行。纯权分母全属当前已付图；没有 D 逆或 D 范数逆。

| 实际返回 | 源内秒数 | 规范定义字节数 | SHA256 |
|---|---:|---:|---|
| 缩放 Z0 六行及原迹 | 19.618355419 | 174541 | 749bc4d76c634b368b43049609c3b9dd60a65bc42416279764533c0131750d9f |
| 缩放 Z1 六行及原迹 | 19.712706086 | 27698 | 1ab7a4a984bce13a8d54356f38e8cd7697620df3ca86d9ccbb1fad0df750b65c |
| 缩放 Z2 六行及原迹 | 19.721735764 | 4176 | 9579bc01b898cf95128d9abed9bb43a828f62ef797ff942b63f5141908dc97a2 |
| 完整 Vlow 六行及来源 | 31.252761980 | 1412526 | bc0e991753015a3d7e4c8c8faeda0b2d4702f38606f4f7df322b9c9b5ed0d681 |

定义字节数只说明实际算得对象的规范序列化大小；这些系数没有保存、打印或分片传输。

## 3. 首次返回的 qT4 两列

qT4 沿[原双四次](../results/R150-appendix-unit211-W-original-two-quartic-necessary-values.md)的 C4 和[首一 T 四次](../results/R150-appendix-unit211-W-global-monic-T-four-F-two-and-finite-original-environments.md)的已付纯权头定义。它的六行只是新 pair 的必要输入，先前已经返回的该六行不重复登记。

本次首次把它的 native 六行一次代入实际 alpha、chi 坐标，并按
$$
q_\alpha=\alpha^2+q_1\alpha+q_0
$$
短除，完整返回
$$
\widehat q_{T4}-[\alpha^2]\widehat q_{T4}\,q_\alpha
=r_0+r_1\alpha.
\tag{3}
$$
源还把两个实际系数清分母乘回。所有尺度只含已付纯权；未知 chi 内容和首项全保留。

(3) 在104.342457268秒完成。其两个清分母列的次数顺序为 (e,k,chi)：

| 列 | 次数 | 总次数 | 项数 | 规范字节数 | SHA256 |
|---|---|---:|---:|---:|---|
| r0 | (92,99,7) | 152 | 43136 | 2359198 | 46c95024ed386570e48187d053959012ffc5c68c53fbcd1f4677285ca09ff7e7 |
| r1 | (88,98,8) | 149 | 45851 | 2474649 | fb44b99f444d4ddeffb19e0812c18bfa5e2efb7ee28828e4051da658bef28dc6 |

它与已有原 I6 十行共同给原 qT4 必要关系。没有把原商当成自由二模；首一 q-alpha 的自由性只用于环境。

## 4. 未完成部分与准确冻结

完整日志最后的数学 checkpoint 是 (3)。之后进入 Vlow 的单次换基块，未出现其线性式完成标记；具体停在该块哪一行没有进一步日志，故不猜测。

以下均未完成：

- Vlow 的 alpha、chi 二列；
- 两值二列完成标记；
- qT4/Vlow 的共同实际乘子、scalar 或参数投影；
- 全 W 排空或新的有限点数界。

这次没有原身份断言失败。真实退出为源 exit -14（SIGALRM），固定180秒触界，峰值 RSS 290824 KiB。该换基与 pair 尾段冻结；不提高预算、重启或只改运行次序。后继必须来自新的原低次结构或不同数学输入。

## 5. 真实执行和源

唯一 actual：run46121350733/job140906380882。

- 源及内层：180.031927720秒；source exit -14。
- source commit：ebfa29f5ace357092d4c69329028afb9741c9e02。
- source blob：2d72202d0ea06794237b67555bf5045755259c39。
- 源 SHA256：c786f55735449210bddef16efc68b4a715f3b3a48e203f85e35bdce5509ea1ef。
- stdout：4075 B，SHA256 4aab0973dc4d0d206a38de006b0e41599c53bc50997ef2c66df4e030d42cbf50。
- 真实 pull：2026-11-28 07:28:37.853631 UTC，至4562d8c809f3ced3a5e8668928702e1b47bb50b3；两 README 未变。

源 basename：
2026-11-28-unit211-W-alpha-chi-scaled-entire-V-first-qT4-pair-8542.py。

原 a96d 和 C9 仅必要定义前缀，旧十行、三个 scalar、R6/Nlow/Plow 目标、旧范数均未执行。此前17703的定义范围失败保留原记录；本次完成的三个缩放基底解决该输入问题，但不能因此把此次尾段超时改写为整体成功。
