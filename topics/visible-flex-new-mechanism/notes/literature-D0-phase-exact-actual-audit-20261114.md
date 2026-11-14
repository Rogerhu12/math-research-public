# D0 局部相位的真实 Fraction 证书审计

日期：2026-11-14。公开 Actions 43596615883 / attempt 1 / exact_D0 已完成，workflow 状态 success。源提交为 ee58536b86a5382851f703199a7dbda4a80e2fac。审读输出 notes/actions-43596615883-1-exact_D0/D0-phase-Fraction-certificate.json 及同目录 receipt.json；本次确由 Python fractions.Fraction 执行，不再只是此前 JavaScript BigInt 预核。

输出 SHA256：d9ae0cc2493f6c96f056f8afeb9018eea1ceab2ff62e41cee0d306354162ba1e。证书脚本 SHA256：a915668c32fa5a68d33923c46ed6ed9af1b4fb512df7ed1bc8250be799c00233。publisher 的最后已读规则提交为 83ec16dd826cb839253d48fce34f0df11456fdec。

实际准确验证了 D=0、B 行列式 4/27、基底三阶 jet、L 二阶系数 −262144/5038605、第四导数 16777216/226737225、解析实基底至12阶递推及 Q 至10阶恒零。横向指标根为 0,1,9/2,−7/2；固定相位幅度的 Euler 根为 0,−9/2,−7/2,−8。各有理数与 R22 正文相符。

有限代数验证不是收敛证明。R22 的真实局部存在性来自正文的加权收缩；本轮没有执行几何优化或数值 ODE，没有构造实际闭基底、完整双端 profile 或有限等距闭曲面族。新 phase_D0 lane 将使用同一精确 Puiseux 系数，在不同起点及截断阶之间作固定 germ 的实际数值验证，并保持局部 J 常数与实际右尾积分的区别。
