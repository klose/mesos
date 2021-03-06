# Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""
Represents an EC2 Elastic IP Volume
"""
from boto.ec2.ec2object import EC2Object

class Volume(EC2Object):
    
    def __init__(self, connection=None):
        EC2Object.__init__(self, connection)
        self.id = None
        self.create_time = None
        self.status = None
        self.size = None
        self.instance_id = None
        self.create_time = None
        self.attach_time = None
        self.device = None
        self.snapshot_id = None
        self.attach_data = None

    def __repr__(self):
        return 'Volume:%s' % self.id

    def startElement(self, name, attrs, connection):
        if name == 'attachmentSet':
            self.attach_data = AttachmentSet()
            return self.attach_data
        else:
            return None

    def endElement(self, name, value, connection):
        if name == 'volumeId':
            self.id = value
        elif name == 'createTime':
            self.create_time = value
        elif name == 'attachTime':
            self.attach_time = value
        elif name == 'instanceId':
            self.instance_id = value
        elif name == 'status':
            if value != '':
                self.status = value
        elif name == 'size':
            self.size = int(value)
        elif name == 'snapshotId':
            self.snapshot_id = value
        elif name == 'device':
            self.device = value
        else:
            setattr(self, name, value)

    def delete(self):
        return self.connection.delete_volume(self.id)

    def attach(self, instance_id, device):
        return self.connection.attach_volume(self.id, instance_id, device)

    def detach(self):
        return self.connection.detach_volume(self.id, self.instance_id)

    def create_snapshot(self):
        return self.connection.create_snapshot(self.id)

    def volume_state(self):
        return self.status

    def attachment_state(self):
        state = None
        if self.attach_data:
            state = self.attach_data.status
        return state

class AttachmentSet(object):
    
    def __init__(self):
        self.id = None
        self.instance_id = None
        self.status = None
        self.attach_time = None
        self.device = None

    def __repr__(self):
        return 'AttachmentSet:%s' % self.id

    def startElement(self, name, attrs, connection):
        pass
    
    def endElement(self, name, value, connection):
        if name == 'volumeId':
            self.id = value
        elif name == 'instanceId':
            self.instance_id = value
        elif name == 'status':
            self.status = value
        elif name == 'attachTime':
            self.attach_time = value
        elif name == 'device':
            self.device = value
        else:
            setattr(self, name, value)

