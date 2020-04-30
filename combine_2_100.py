import os

filepath = '/Users/jingxiaoxian/Documents/GitHub/L2_Sensitivity/pk323c_eps/'
cmd = 'mkdir ' + filepath + '5'
os.system(cmd)
exp_id_list = set()
for _ in [f for f in os.listdir(filepath+'1/')]:
    tmp = _.split('_')
    if tmp[0][0] in '1234567890':
        exp_id_list.add(tmp[0])


for exp_id in exp_id_list:
    exp_plot = []
    for _ in [f for f in os.listdir(filepath+'1/')]:
        if _.startswith(exp_id+'_'):
            exp_plot += [' '+_+' ']
            cmd = 'cp '+ filepath+  '1/' + _ + ' ./'
            os.system(cmd)
    for _ in [f for f in os.listdir(filepath+'2/')]:
        if _.startswith(exp_id+'_'):
            exp_plot += [' '+_+' ']
            cmd = 'cp '+ filepath+  '2/' + _ + ' ./'
            os.system(cmd)
    cmd = 'bash pdfcat ' + '  '.join(exp_plot)
    os.system(cmd)
    for _ in exp_plot:
        cmd = 'rm ' + _
        os.system(cmd)
    cmd = 'mv allfigs.pdf '+filepath+'5/' + exp_id + '_comb.pdf'
    os.system(cmd)


