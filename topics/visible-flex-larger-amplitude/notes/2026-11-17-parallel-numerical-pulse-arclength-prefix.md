# 正确 pulse 度量下直到 s=1 的完整规范化前缀

**数值证据；新的开放 C² 候选，不是 BVP 接受或闭面完成。** 使用已接受 d644 前缀的全部498个胞元，精确零补至M320；接上真实 pulse 局部场的320胞。两者切口s=.995的0/1/2jet逐位相同，拼接时只去掉重复切口节点。完整818胞、s∈[0,1]统一按固定q_N4096弧长规范化，audit8192角/每胞4分点共26,812,416点，最大relative Gram为 **1.97440804930e−7**。未规范化的同一拼接场、同样本为1.31242503904e−6。

## 源和共同场

- 左父 `parallel-continue0995-m112.json.gz`：SHA256 `d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f`，M112/N2048。
- 右场 `parallel-pulse-a5-fullfield-n4096-c2.json.gz`：`381de9825a713e301787ef67f0d694e288bea2e920d6b269b9240e90e9d3851a`，M320/N4096。它来自原有限Fourier IVP与显式C²共享jet修补，metadata明确bvp_accepted=false。
- 实际 PulseProfile 源 `notes/2026-11-17-parallel-inward-curvature-pulse.py`：`148dd6305df67c881ceb180249f4eaf34e3a996a6568c7378be467d41a92d157`。幅度−5、半宽.005；其余κ1.5、两.02 ramp、Gauss32参数均读取右场完整scalar描述。没有用忽略pulse的旧profile读者。

左侧二jet先在原M112/N2048、原Profile上作原JVP，再逐分量零补到M320；右侧保持其保存的d2。没有以提升后的M320方程重造左侧加速度，也没有把几何candidate伪标为accepted。所有公共二jet再定义唯一分片五次式。核心角密度与右场original_core_coefficients逐位核同；新度量在cut前与原父相同，cut后为明确的pulse新设计。

整个拼接场一起应用[固定弧长规范化](2026-11-17-parallel-numerical-arclength-normalized-prefix.md)，两侧使用同构造N、同ρ和同基点。曲率在同像G=c+λ(F−c)上用真实λ′/λ″计算；所有metric余项，包括角项(q/q_N)²−1，均实际保留。共同C²的正性条件仍沿该定义；本轮只作采样读数及每个采样s处的全角Lipschitz正性下界。

## 实际结果

最坏Gram位于s=.9997890624999888、旧角2.6652916189513；rr=−1.88185820926e−7，角项−3.00e−15，混合项−4.27470638004e−8。最大主曲率6.98222344867，位于s=1、旧角.0168737886667。

全样本|λ−1|≤2.295e−12、|λ′|≤1.954e−8、|λ″|≤.000288701；角metric余项≤4.486e−14。按相同旧角匹配的像点缩放差≤3.314e−12，不将此解释为相同材料点位移。核心0/1/2jet读数差为3.14e−16/0/2.54e−16。采样q_N最小.16601843，逐采样s的全角下界≥.15909568。曲率不是reach证书，整个prefix仍未闭合、未查全t；同g重新求解的精化收敛未由此次坐标变换支付。

## 复现

S为本题scripts目录。raw与拼接状态仅scratch。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_pulse_arclength_readout.py" --parent parallel-continue0995-m112.json.gz --local parallel-pulse-a5-fullfield-n4096-c2.json.gz --pulse-source "$S/../notes/2026-11-17-parallel-inward-curvature-pulse.py" --assembled parallel-pulse-a5-complete-base.json.gz --construction-angles 4096 --angles 8192 --radial-subdivisions 4 --out parallel-pulse-a5-complete-arclength-c4096-a8192.json
```

源码SHA256 `31782ba06d5414a7851284ce330a89d208b8d56c4f1d99421a804e2a78271266`；拼接base输出 `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`；实际readout输出 `43b56fffa44abcbe24d4e72ec069a180b0d87684eb61d35f5670e4ba00ac425a`。原父、右局部场、规范化新候选各有独立身份，不能互相代作新BVP父。

## 同一 pulse 候选的径向读出加密

固定构造q_N4096与audit8192，只将每胞径向4分点改为8分点，818胞共53,616,640点。最大Gram为 `1.9744113275415063e−7`，较首轮增加 `3.27824e−13`，最坏点s=.999787109375、旧角.476301034638。κmax保持 `6.982223448666474`；角余项max `4.797e−14`。拼接输入仍为同一 `26e53e8c...`，切口六jet仍逐位同一，未新求解或改变候选。

沿原命令设 `--radial-subdivisions 8`；拼接输出临时名 `parallel-pulse-a5-complete-base-refread.json.gz`，其字节身份与首轮相同。readout为 `parallel-pulse-a5-complete-arclength-c4096-a8192-r8.json`，SHA256 `93bf4e39427d470bd3dd2e7400561f42715ef37451b46bacc9b484ee1cc43b0c`。本次仅为已有候选短quintic胞元峰值的读出核对，不计作README第5项固定参数重新求解收敛。
